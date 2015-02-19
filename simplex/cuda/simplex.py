import pycuda.autoinit
import numpy
from pycuda.compiler import SourceModule
from pycuda import gpuarray, compiler
import time


def log(string):
    print time.strftime("%Y-%m-%d-%H-%M-%S", time.gmtime()) + ":\n" + str(string)
def compute_cuda_simplex(matrix ,  basics_index , is_max):
    SourceModule = ("""
        /// compute the divide of b / column_k
    __global__ void kernel1(float simplex[%(M)s][%(N)s] , float* teta , float* columnK , int k ){
        int idx = blockDim.x * blockIdx.x + threadIdx.x ;
        float w = simplex[idx][k] ;
        /* copy the weights of entering index k */
        columnK[idx] = w;
        teta[idx] = simplex[idx][0]/w;
    }

        /// compute the divide of row[r]/ pivot[r]
    __global__ void kernel2(float simplex[%(M)s][%(N)s] , float* columnK ,  int k , int r){
        int idx = blockDim.y * blockIdx.y + threadIdx.y;
        __shared__ float w;
        /* Get the pivot element : simplex[r][k] in the shared memory */
        if(threadIdx.x == 0) w = columnK[r];
        __syncthreads();
        /*Update the line of leaving index r*/
        simplex[r][idx] = simplex[r][idx]/w;
    }

        ///Compute the row[a] - (row[r]/pivot[r] * pivot[a])
    __global__ void kernel3(float simplex[%(M)s][%(N)s] , float* columnK , int k , int r){
        int idx = blockDim.y * blockIdx.y + threadIdx.y;
        int jdx = blockIdx.x * blockDim.x + threadIdx.x;
        __shared__ float w[16];
        /* Get the column of entering index k in shared memory */
        
        w[threadIdx.x] = columnK[blockIdx.x * blockDim.x + threadIdx.x];
        
        __syncthreads();
        /* Update the basis except the line r */

        if(jdx == r) return;
        
        simplex[jdx][idx] = simplex[jdx][idx] - w[threadIdx.x]*simplex[r][idx];
    }


    __global__ void kernel4(float simplex[%(M)s][%(N)s] , float*  columnK , int k , int r){
        int jdx = blockDim.x*blockIdx.x + threadIdx.x;
        // __shared__ float w;
        /* Get the pivot element : simplex[r][k] in the shared memeory */
        //if(threadIdx.x == 0  ) w = columnK[r];
        __syncthreads();
        /* Update the column of the entering index k */
        if(jdx != r) simplex[jdx][k] = 0;

        /* Update the pivot element simplex[r][k] */
        if(jdx == r) simplex[jdx][k] = 1;
    }
      """)
    # print "booooooogh" , slacks_indices
    h = int((numpy.shape(matrix)[0]) / 16) 
    w = int((numpy.shape(matrix)[1]) / 32) 

    # h = int(len(matrix)/16)
    # w = int(len(matrix[0])/32)
    
    columnK = numpy.zeros(shape=(16*h)).astype(numpy.float32)
    teta = numpy.zeros(shape=(16*h)).astype(numpy.float32)
    matrix_gpu  = gpuarray.to_gpu(matrix)
    teta_gpu = gpuarray.to_gpu(teta)
    columnK_gpu = gpuarray.to_gpu(columnK)
    # basics_index = []

    counter = 0
    

    SourceModule_e = SourceModule%{
        'N' : w * 32,
        'M' : h * 16,
    }
    # row = matrix_gpu.get()[0]
    while(True):
        k = 0 
        r = 0
        # print "matrix : \n" , matrix
        #print "iterate :" , counter
        #print "basics_index :" , basics_index
        counter+=1
        #print "boogh \n" ,  matrix_gpu.get()
        # log(" i =  " + str(counter) + "matrix :\n" )
        # print_matrix(matrix_gpu.get())
        row = matrix_gpu.get()[0]
        #print "row= ", row
        k = -1
        if is_max:
            minimum = 0
            i  = 0 
            # Find the index of entering variable k
            for item in row :
                if i == 0 :
                    i = i +1 
                    continue
                if item < minimum :
                    minimum = item
                    k = i
                    row[i] = 0
                i = i + 1
            if minimum >= 0 :
                solution = matrix_gpu.get()[0][0]
                basics_value = matrix_gpu.get()[1:,0]
                A = matrix_gpu.get()[1:,1:]
                #print " before return \n" , matrix_gpu.get()
                return { "A" : A , "solution" : solution , 
                "basics_value" : basics_value , "basics_index" : basics_index}
            #print "minimum" , minimum

        else:
            maximum = 0
            i = 0 
            #print row
            for item in row :
                if i == 0 :
                    i = i +1 
                    continue
                if item > maximum :
                    maximum = item
                    k = i
                    row[i] = 0
                i = i + 1
            if maximum <= 0 :
                solution = matrix_gpu.get()[0][0]
                basics_value = matrix_gpu.get()[1:,0]
                A = matrix_gpu.get()[1:,1:]
                #print " before return \n" , matrix_gpu.get()
                return { "A" : A , "solution" : solution , "basics_value" : basics_value , 
                "basics_index" : slacks_indices}
            #print "maximum" , maximum

        mod = compiler.SourceModule(SourceModule_e)
        kernel1 = mod.get_function("kernel1")
        #print "k : " , k
        kernel1(matrix_gpu , teta_gpu ,  columnK_gpu , numpy.int32(k) , block=(16 , 32 ,1 ) ,
         grid=(h , w  , 1))

        #print "kernel1 out matrix\n" ,matrix_gpu.get()

        flag = False
        minimum = -1
        # print "i :" , i
        ##print "k :" , k
        #print "teta_gpu:\n", teta_gpu.get()
        i = 0 
        for i in range (1 , h * 16):
            if minimum == -1 and teta_gpu.get()[i] > 0:
                minimum = teta_gpu.get()[i]
                flag = True
                r = i
            elif teta_gpu.get()[i] > 0 and teta_gpu.get()[i] < minimum:
                minimum = teta_gpu.get()[i]
                r = i
        if not flag :
            # print "unbounded"
            log("unbounded problem")
            #print "A : \n" , matrix_gpu.get()
            break

        #print "r is :" , r
        kernel2 = mod.get_function("kernel2")
        # print "kernel1 out matrix\n" ,matrix_gpu.get()
        kernel2(matrix_gpu , columnK_gpu , numpy.int32(k), numpy.int32(r) , block=(16 , 32 , 1) , 
            grid=( h , w  , 1))

        # print "r :" , r
        # print "kernel2 out matrix\n" ,matrix_gpu.get()
        kernel3 = mod.get_function("kernel3")

        kernel3(matrix_gpu , columnK_gpu , numpy.int32(k), numpy.int32(r) , block=(16 , 32 , 1) ,
         grid=(h , w , 1))

        # print "kernel3 out matrix\n" ,matrix_gpu.get()
        kernel4 = mod.get_function("kernel4")
        kernel4(matrix_gpu , columnK_gpu , numpy.int32(k), numpy.int32(r) , block=(16 , 32 , 1) ,
         grid=(h , w , 1))
        #print "kernel4 out matrix\n" ,matrix_gpu.get()
        slacks_indices[r-1] = k



# print matrix 
def print_matrix(m):
    print ("***")
    s = [[str(e) for e in row] for row in m]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\n'.join(table))
    print ("***")

#returns k'th column of a 2d matrix
def column(matrix, i):
    return [row[i] for row in matrix]

#set the k'th column of a 2d array 0
def set_column_zero(matrix , j):
    for i in range(len(matrix)):
        matrix[i][j] = 0.0

#compute simplex with A , B and C 
def cuda_simplex(A , B , C , basics , is_max):
    m = len(A)
    if m <= 0 :
        return
    n = len(A[0])
    A = numpy.concatenate(([C], A), axis=0)
    matrix = numpy.zeros(shape=((round((numpy.shape(A))[0]/16) + 1)*16 ,
        (round((numpy.shape(A))[1]/32) + 1 )*32)).astype(numpy.float32)
    for i in range (m +1):
        for j in range (n + 1):
            if(j == 0 ):
                matrix[i][j] = B[i]
            else:
                matrix[i][j] = float(A[i][j-1]) 
    return_collection = compute_cuda_simplex(matrix , basics , is_max)
    #print "solution: " ,return_collection["solution"]
    # print "basics :" , return_collection["basics_index"]
    #print "A :" , return_collection["A"]
    #print "B :" , return_collection["basics_value"] 

    A = return_collection["A"]
    basics = return_collection["basics_index"]
    B = return_collection["basics_value"]
    solution = return_collection["solution"]
    values = numpy.zeros(len(A[0]))
    # print "A " , A
    # print "basics" , basics
    # print "solution" , solution
    for i in range(len(A)):
        if(i >= len(basics)):
            break
        values[basics[i] - 1 ] = B[i] / A[i][basics[i]-1]
    # log("values " + str(values))
    # log("solution " + str(solution))
    return {"A": A , 
    "B" : B , 
    "basics": basics ,
    "solution" : solution , 
    "values" : values}


def find_feasible_point(A,B,C,virtuals_constraints_num, virtuals_indices, 
    slacks_constraint_num , slacks_indices , is_max ):
    feasible_point = numpy.zeros(len(C))
    #print "slacks_indices :" , slacks_indices
    if len(virtuals_indices) == 0 :# Compute cuda in one step
        res = cuda_simplex(A , B , C , slacks_indices , is_max)
        final_result = 0.0
        for i in range(len(values)):
            final_result += res["values"][i] * final_target[i]
        return { "values" : res["values"] , "result" : final_result}
    else:#Compute cuda in 2 phase
        Target = numpy.copy(C)
        C = numpy.zeros(shape=(len(C)-len(virtuals_constraints_num),1))
        basics = numpy.zeros(shape=(len(B)-1 , 1))
        #create target to minimize the sum of virtual variables
        for i in range(len(virtuals_indices)):
            C = numpy.append(C , [-1.0])
        #print "C is :" , C

        # kanooni kardan bar hasb virtual ha 
        for i in range(len(virtuals_constraints_num)):
            for j in range(len(C)):
               C [j] +=  A[virtuals_constraints_num[i]-1][j]
            B[0] += B[virtuals_constraints_num[i]]
            ## set the virtuals as basics
            basics [virtuals_constraints_num[i]-1] = virtuals_indices[i]
        
        ## set the slacks as basics where no virtual is available
        for i in range(len(slacks_constraint_num)):
            if(basics[slacks_constraint_num[i]-1] == 0 ):
                basics[slacks_constraint_num[i]-1] = slacks_indices[i]

        ret = cuda_simplex(A , B , C , basics , False)
        A = ret["A"]
        B = ret ["B"]
        basics = ret["basics"]
        values = ret["values"]
        # log( "basics : " + str(basics))
        
        if (ret["solution"] >= 0.0001 ):# x6+x7 !=0
            log("not Find feasible region in Phase 1")
            # print ("not Find feasible region in Phase 1")
        else:
            C = Target
            final_target = numpy.copy(Target)
            # log("target :" + str(C))
            while len(A[0]) != len(C):
                C = numpy.append(C , [0.0])
            final_target = numpy.copy(C)
            target_sum = 0.0
            for i in range(len(values)):
                target_sum += values[i] * C[i]

            for i in range (len(basics)):
                if(C[int(basics[i])-1] != 0):
                    piv = C[int(basics[i])-1] / A[i][int(basics[i])-1]
                else:
                    piv = 0.0 
                temp = []
                #print " A  " , len(A) , " A[0]" , len(A[0])
                # log("A :\n" + str(A))
                # log("C :\n" + str(C))
                # log("B :\n" + str(B))
                # log("target_sum :\n" + str(target_sum))
                for k in range(len(A[i])): 
                    temp.append( A[i][k] * piv)
                    
                len_C = len(C)
                
                # log("temp : " + str(temp))
                # log("before :C :\n" + str(C))
                for p in range( len(temp) ):
                    C[p] = float(C[p]) -  float(temp[p])
                # log("after :C :\n" + str(C))
                
                target_sum -=B[i] * piv
                for j in range ( len(basics) ):
                   if ( j!=i ):
                       if( A[i][int(basics[i])-1] != 0 ):
                           piv = A[j][int(basics[i])-1] / A[i][int(basics[i])-1]
                       else:
                           piv = 0.0 ;
                       temp = []
                       for k in range(len(A[i])):
                           temp.append( A[i][k] * piv)
                       for p in range(len(A[i])):
                           A[j][p] -= temp[p]

            b2 = B
            c_temp = C[len_C-1]
            numpy.append([c_temp] , b2)

            # print "A : ------------------------------- \n" , A
            # print " virtuals_indices" , virtuals_indices
            for i in virtuals_indices:
                set_column_zero(A , i-1)
                C[i-1] = 0.0
            # print "A : ++++++++++++++++++++++++++++++++\n" , A
            
            #print "basics" , basics
            #print_matrix (A)
            b2 = numpy.append([target_sum] , b2)
            #print "before getting unbounded"
            #print "C:"
            #print (C)
            #print "b2:"
            #print (b2)
            
            res = cuda_simplex(A,b2,C,basics,is_max )
            final_result = 0.0
            # print "booogh1 " , len(res["values"])
            # print "boogh2" , len(final_target)
            for i in range(len(values)):
                final_result += res["values"][i] * final_target[i]
            return { "values" : res["values"] , "result" : final_result}
    return






# A = numpy.array([
#      [8,12,-1,0,0,0,1,0,0]
#     ,[12,12,0,-1,0,0,0,1,0]
#     ,[2,1,0,0,-1,0,0,0,1]
#     ,[1,1,0,0,0,1,0,0,0]
#     ])
# C = numpy.array([0.2,0.3,0,0,0,0,0,0,0])
# B = numpy.array([0 , 24,36,4,5])
# # x      y      s1     s2     s3     s4
# x = numpy.array(['x','y','s1','s2','s3','s4','z1' , "z2" , "z3"])
# virtuals_indices=numpy.array([ 7 , 8 , 9])
# virtuals_constraints_num=numpy.array([1, 2 , 3 ])
# slacks_constraint_num=numpy.array([1,2,3,4])
# slacks_indices=numpy.array([3 , 4, 5 , 6])


# A = numpy.array([[1,1,-1,0,0,1,0],[-1,1,0,-1,0,0,1],[0,1,0,0,1,0,0]])
# C = numpy.array([-1,+2,0,0,0,0,0])
# B = numpy.array([0,2,1,3])
# x = numpy.array(['x1','x2','x3','x4','x5','x6','x7'])
# virtuals_indices=numpy.array([6 , 7])
# virtuals_constraints_num=numpy.array([1, 2])
# slacks_constraint_num=numpy.array([1,2,3])
# slacks_indices=numpy.array([3 , 4, 5])

# A = numpy.array([
#      [1,1,-1,0,1]
#     ,[1,-1,0,1,0]
#     ])
# C = numpy.array([1,2,0,0,0])
# B = numpy.array([0,2,2])
# # x      y      s1     s2     s3     s4
# x = numpy.array(['x','y','s1','s2','z1'])
# virtuals_indices=numpy.array([5])
# virtuals_constraints_num=numpy.array([1])
# slacks_constraint_num=numpy.array([1,2])
# slacks_indices=numpy.array([3 , 4])

A = numpy.array([
     [1,1,-1,0,0,1]
    ,[1,1,0,1,0,0]
    ,[-(1/3) , 1 ,0,0,1,0]
    ])
C = numpy.array([0.05,0.04,0,0,0,0])
B = numpy.array([0,10,12 , 0])
# x      y      s1     s2     s3     s4
x = numpy.array(['x','y','s1','s2','s3' , 'z1'])
virtuals_indices=numpy.array([6])
virtuals_constraints_num=numpy.array([1])
slacks_constraint_num=numpy.array([1,2,3])
slacks_indices=numpy.array([3 , 4 ,5])


log("Starting")
#find_feasible_point(A, B, C, virtuals_indices, slacks_indices)
result = find_feasible_point(A,B,C,virtuals_constraints_num, virtuals_indices, slacks_constraint_num , slacks_indices , False)
log( "result \n\n" + str(result))

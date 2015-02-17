import pycuda.autoinit
import numpy
from pycuda.compiler import SourceModule
from pycuda import gpuarray, compiler


def compute_cuda_simplex(matrix ,  basics_index ):
    SourceModule = ("""
    __global__ void kernel1(float simplex[%(M)s][%(N)s] , float* teta , float* columnK , int k ){
        int idx = blockDim.x * blockIdx.x + threadIdx.x ;
        float w = simplex[idx][k] ;
        /* copy the weights of entering index k */
        columnK[idx] = w;
        teta[idx] = simplex[idx][0]/w;
    }


    __global__ void kernel2(float simplex[%(M)s][%(N)s] , float* columnK ,  int k , int r){
        int idx = blockDim.y * blockIdx.y + threadIdx.y;
        __shared__ float w;
        /* Get the pivot element : simplex[r][k] in the shared memory */
        if(threadIdx.x == 0) w = columnK[r];
        __syncthreads();
        /*Update the line of leaving index r*/
        simplex[r][idx] = simplex[r][idx]/w;
    }


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
        __shared__ float w;
        /* Get the pivot element : simplex[r][k] in the shared memeory */
        if(threadIdx.x == 0  ) w = columnK[r];
        __syncthreads();
        /* Update the column of the entering index k */
        simplex[jdx][k] = -columnK[jdx]/w;

        /* Update the pivot element simplex[r][k] */
        if(jdx == r) simplex[jdx][k] = 1/w;
    }
      """)
    
    h = int((numpy.shape(matrix)[0]) / 16) 
    w = int((numpy.shape(matrix)[1]) / 32) 

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
    row = matrix_gpu.get()[0]
    while(True):
        k = 0 
        r = 0
        print "iterate :" , counter
        
        print "r :" , basics_index
        counter+=1
        # print matrix_gpu.get()
        # row = matrix_gpu.get()[0]
        minimum = 0
        i  = 0 
        # Find the index of entering variable k
        for item in row :
            if item < minimum :
                minimum = item
                k = i
                row[i] = 0
            i = i + 1
        if minimum >= 0 :
            solution = matrix_gpu.get()[0][0]
            basics_value = matrix_gpu.get()[1:,0]
            A = matrix_gpu.get()[1:,1:]
            return { "A" : A , "solution" : solution , "basics_value" : basics_value , "basics_index" : basics_index}

        mod = compiler.SourceModule(SourceModule_e)
        kernel1 = mod.get_function("kernel1")
        print "k : " , k
        kernel1(matrix_gpu , teta_gpu ,  columnK_gpu , numpy.int32(k) , block=(16 , 32 ,1 ) ,
         grid=(h , w  , 1))

        # print "kernel1 out matrix\n" ,matrix_gpu.get()

        flag = False
        minimum = -1
        # print "i :" , i
        # print "k :" , k
        # print "teta_gpu:\n", teta_gpu.get()
        i = 0 
        for i in range (0 , m + 1):
            if minimum == -1 and teta_gpu.get()[i] > 0:
                minimum = teta_gpu.get()[i]
                flag = True
                r = i
            elif teta_gpu.get()[i] > 0 and teta_gpu.get()[i] < minimum:
                minimum = teta_gpu.get()[i]
                r = i
        if not flag :
            print "unbounded"
            break


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
        # print "kernel4 out matrix\n" ,matrix_gpu.get()
        basics_index[r-1] = k + 1



def cuda_simplex(A , B , C , basics):
    m = len(A)
    if m <= 0 :
        return
    n = len(A[0])
    #B = [0] + B
    A = [C] + A
    for i in range (0 , m +1 ):
        print B[i]
        A[i] = [B[i]] + A[i]

    print "glhglkh" ,A    
    ccs = compute_cuda_simplex(A , basics)
    return {"A": ccs["A"] , "B" : ccs["basics_value"] , "basics":ccs["basics_index"]}


def find_feasible_point(A,B,C,virtuals_constraints_num, virtuals_indices, slacks_constraint_num , slacks_indices ):
#def find_feasible_point(A, B, C, virtuals_indices, slacks_indices):
    feasible_point = numpy.zeros(len(C))

    if len(virtuals_indices) == 0 :
        return cuda_simplex(A , B , C , slacks)
    else:
        CBasic = C
        C = [0] * (len(C)-len(virtuals_constraints_num)) # C = [0,0,0,0,0]
        basics = [0] * (len(B)-1) # basics= [0,0,0]
        for i in range(len(virtuals_indices)):
            C.append(-1)
        print (" C=  " , C) # C= [0,0,0,0,0,-1,-1]
        for i in range(len(virtuals_constraints_num)):
            for j in range(len(C)):
                C [j] +=  A[virtuals_constraints_num[i]-1][j]
            B[0] += B[virtuals_constraints_num[i]]
            basics [virtuals_constraints_num[i]-1] = virtuals_indices[i]
        print (" C=  " , C )# C= [0,2,-1,-1,0,0,0] C kanooni shode
        # B[0] = 3
        # basics = [6,7,0]
        for i in range(len(slacks_constraint_num)):
            if(basics[slacks_constraint_num[i]-1] == 0 ):
                basics[slacks_constraint_num[i]-1] = slacks_indices[i]
        print ("Normilized Phase#1")
        print "Basic:",basics # basics = [6,7,5]
        print "constraint:",C # C = [0,2,-1,-1,0,0,0]
        # phase #1 Simplex
        ret = cuda_simplex(A , B , C , basics)########?????????????????????????????????
        A = ret["A"]
        B = ret ["B"]
        basics = ret["basics"]

        #farz : A, B, C , basics avaz shodand 
        
        #basics = [1,2,5]

        if (abs(C[len(C)-1]) >= 0.0001 ):# x6+x7 !=0
            print ("not Find feasible region in Phase 1")
        else:
            # start phase #2 Simplex
            C = CBasic
            C.append(0)
            # C = [-1,2,0,0,0,0,0,0] 
            for i in range (len(basics)):
                if(C[basics[i]-1] != 0):
                    piv = C[basics[i]-1] / A[i][basics[i]-1]
                else:
                    piv = 0 ;
                # piv (i = 0) => -1
                # piv (i = 1) => 2
                # piv (i = 2) => 0
                temp = []
                for k in range(len(A[i])): 
                    temp.append( A[i][k] * piv)
                for p in range(len(A[i])):
                    C[p] -= temp[p]
                # C[all basics] = 0
                # C = [0,0,1/2,3/2,0,0,0,-5/2]
                for j in range (len(basics)):
                   if (j!=i):
                       if(A[i][basics[i]-1] != 0):
                           piv = A[j][basics1_int[i]-1] / A[i][basics1_int[i]-1]
                       else:
                           piv = 0 ;
                       temp = []
                       for k in range(len(A[i])):
                           temp.append( A[i][k] * piv)
                       for p in range(len(A[i])):
                           A[j][p] -= temp[p]
            print ('normilized Phase#2')
            b2 = column(A,len(A[0])-1)
            c_temp = c[len(c)-1]
            b2.insert(0,c_temp)
            c.pop(len(c)-1)
            A2 = pop_column(A,len(A[0])-1)
            virtual_str = [x[1:] for x in virtuals]
            virtual_int = [int(s) for s in virtual_str if s.isdigit()]
            virtual_int.reverse()
            for i in range(len(virtual_int)):
                A2 = pop_column(A2,virtual_int[i]-1)
                c.pop(virtual_int[i]-1)
            basics2 = [0] * len(basics1_int)
            for i in range(len(basics1_int)):
                basics2[i] = 'x' + str( basics1_int[i])
            print_matrix (A2)
            print (c)
            print(b2)
            print(basics2)
            simple_simplex(A2,c,b2,x,basics2,is_max )

    return


n = 2
m = 3

C = -1 * [ 15 , 10]
B = [ 2 , 3 , 4]
A = [[1 , 0], [0 , 1]  , [1 , 1]]


A = [[1,1,-1,0,0,1,0],[-1,1,0,-1,0,0,1],[0,1,0,0,1,0,0]]
C = [-1,2,0,0,0,0,0]
B = [0,2,1,3]
x = ['x1','x2','x3','x4','x5','x6','x7']
virtuals_indices=[6 , 7]
virtuals_constraints_num=[1, 2]
slacks_constraint_num=[1,2,3]
slacks_indices=[3 , 4, 5]


#find_feasible_point(A, B, C, virtuals_indices, slacks_indices)
find_feasible_point(A,B,C,virtuals_constraints_num, virtuals_indices, slacks_constraint_num , slacks_indices )

#cuda_simplex(A , B , C)


# matrix[0][0] = 0
# matrix[0][1] = -15
# matrix[0][2] = -10
# matrix[1][0] = 2
# matrix[1][1] = 1
# matrix[1][2] = 0
# matrix[2][0] = 3
# matrix[2][1] = 0
# matrix[2][2] = 1
# matrix[3][0] = 4
# matrix[3][1] = 1
# matrix[3][2] = 1






# ######
# n = 2
# m = 3


matrix = numpy.zeros(shape=((round((numpy.shape(A))[0]/16) + 1)*16 ,(round((numpy.shape(A))[1]/32) + 1 )*32)).astype(numpy.float32)
#matrix = numpy.zeros(shape=(16 , 32)).astype(numpy.float32)
#matrix = numpy.zeros(shape=(m + 1 , n + m + 1)).astype(numpy.float32)

#0, 1, 2, 1, 0, 0, 7, 9, 8, 0, 1, 0, 5, 10, 0, 0, 0, 1
matrix[0][0] = 0
matrix[0][1] = -15
matrix[0][2] = -10
matrix[1][0] = 2
matrix[1][1] = 1
matrix[1][2] = 0
matrix[2][0] = 3
matrix[2][1] = 0
matrix[2][2] = 1
matrix[3][0] = 4
matrix[3][1] = 1
matrix[3][2] = 1

print "booogh" , matrix 

# # matrix[0][0] = 3
# # matrix[0][1] = 2
# # matrix[1][0] = 2
# # matrix[1][1] = 2

# # matrix[0][0] = 1
# # matrix[0][1] = 0
# # matrix[0][2] = 0
# # matrix[1][0] = 0
# # matrix[1][1] = 1
# # matrix[1][2] = 0
# # matrix[2][0] = 0
# # matrix[2][1] = 0
# # matrix[2][2] = 1
# identity = numpy.identity(m).astype(numpy.float32)
# GaussJordan = numpy.zeros(shape=(16, 32)).astype(numpy.float32)

# GaussJordan_gpu = numpy

# for i in range (0 , m + 1) :
#     for j in range (0 , n + 1):
#         GaussJordan[i][j] = matrix[i][j]

# for i in range (1 , m + 1 ):
#     for j in range ( n + 1 , m + n + 1):
#         GaussJordan[i][j] = identity[i- 1][j -n -1];

# cuda_simplex(GaussJordan)

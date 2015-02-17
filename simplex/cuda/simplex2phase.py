import pycuda.autoinit
import numpy
from pycuda.compiler import SourceModule
from pycuda import gpuarray, compiler


def compute_cuda_simplex(matrix , x_list , basics_index ):
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
        print "x :" , x_list
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





def cuda_simple_simplex(A,c,b,x,slack,is_max ):
    m = len(A)
    if m <= 0 :
        return
    n = len(A[0])

    if not is_max:
        c = c * -1
    # B = [0] + B
    A = [C] + A
    for i in range (0 , m +1 ):
        A[i] = [B[i]] + A[i]
    matrix = numpy.zeros(shape=((round((numpy.shape(A))[0]/16) + 1)*16 ,
        (round((numpy.shape(A))[1]/32) + 1 )*32)).astype(numpy.float32)
    for i in range (m +1):
        for j in range (n + 1):
            matrix[i][j] = float(A[i][j])
    final = compute_cuda_simplex(matrix , x , slack)
    final["A"] = final["A"][0:m , 0:n]
    final["basics_value"] = final["basics_value"][0:m]
    print " final ", final
    return final

def cuda_two_phase_simplex(A,c,b,x,slacks,slack_constraint_number,virtuals , virtual_constraint_number ,is_max ):
    if len(virtuals) ==0 :
        return cuda_simple_simplex(A,c,b,x,slacks,is_max)
    else:
        c1 = [0] * (len(c)-len(virtuals))
        basics1 = [0] * (len(b)-1)
        for i in range(len(virtuals)):
            c1.append(-1)
        for i in range(len(virtual_constraint_number)):
            for j in range(len(c1)):
                c1 [j] +=  A[virtual_constraint_number[i]-1][j]
            b[0] += b[virtual_constraint_number[i]]
            basics1 [virtual_constraint_number[i]-1] = virtuals[i]
        for i in range(len(slag_constraint_number)):
            if(basics1[slag_constraint_number[i]-1] == 0 ):
                basics1[slag_constraint_number[i]-1] = slags[i]
        print ("Normilized Phase#1")
        # print_matrix(A)
        print ("c1=  " , c1)
        print ("b =  " , b)
        print ("basics1=  " , basics1)
        result = cuda_simple_simplex(A,c1,b,x, slacks,0)

        if result["solution"] != 0:
            print "no feasible region"
            return
        #Phase#2
        basics1_int = result["basics_index"]
        c = [0] + c
        print ("Pashe #2")
        A = result["A"] + result["basics_value"]
        # print_matrix(A)
        print ('c',c)
        print ('basics',basics1_int)
        print('b',result["basics_value"])
        for i in range (len(basics1_int)):
            if(c[basics1_int[i]-1] != 0):
                piv = c[basics1_int[i]-1] / A[i][basics1_int[i]-1]
            else:
                piv = 0 ;
            temp = []
            for k in range(len(A[i])):
                temp.append( A[i][k] * piv)
            for p in range(len(A[i])):
                c[p] -= temp[p]
            for j in range (len(basics1_int)):
               if (j!=i):
                   if(A[i][basics1_int[i]-1] != 0):
                       piv = A[j][basics1_int[i]-1] / A[i][basics1_int[i]-1]
                   else:
                       piv = 0 ;
                   temp = []
                   for k in range(len(A[i])):
                       temp.append( A[i][k] * piv)
                   for p in range(len(A[i])):
                       A[j][p] -= temp[p]
        print ('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print ('normalized Phase#2')
        
        b2 = column(A,len(A[0])-1)
        c_temp = c[len(c)-1]
        b2.insert(0,c_temp)
        c.pop(len(c)-1)
        A2 = pop_column(A,len(A[0])-1)
        # print_matrix (A2)
        print ( c)
        print ( b2 )
        print (basics1_int)

        return cuda_simple_simplex(A2,c,b2,x,basics1_int,is_max)


# n = 2
# m = 3

# C = [ -15 , -10 , 0 , 0 , 0 ]
# B = [0 , 2 , 3 , 4]
# A = [[1 , 0, 1 , 0 ,0 ], [0 , 1 , 0 , 1 , 0]  , [1 , 1 , 0 , 0 , 1]]

# cuda_simple_simplex(A , B , C , ['x1' , 'x2' , 's1' ,'s2' ,'s3'] , [3,4,5] , True)

A = [[1,1,-1,0,0,1,0],[-1,1,0,-1,0,0,1],[0,1,0,0,1,0,0]]
c = [-1,2,0,0,0,0,0]
b = [0,2,1,3]
x = ['x1','x2','x3','x4','x5','x6','x7']

is_max = 0 ;
is_2_phase = 1 ;
if (is_2_phase):
    slags = ['x3','x4','x5']
    slag_constraint_number = [1,2,3]
    virtuals = ['x6','x7']
    virtual_constraint_number = [1,2]
    cuda_two_phase_simplex(A,c,b,x,slags,slag_constraint_number,virtuals, virtual_constraint_number ,is_max )
else:
    slags = ['x3','x4','x5','x6','x7']
    cuda_simple_simplex(A,c,b,x,slags,is_max )
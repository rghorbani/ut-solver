import pycuda.autoinit
import numpy
from pycuda.compiler import SourceModule
from pycuda import gpuarray, compiler


def compute_cuda_simplex(matrix , x_list , basics ):
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
        print "r :" , basics
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
            print "solution is here\n" , matrix_gpu.get()
            break

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
        basics[r-1] = x_list[k]



def cuda_simple_simplex(A,c,b,x,slack,is_max ):
    m = len(A)
    if m <= 0 :
        return
    n = len(A[0])

    # B = [0] + B
    A = [C] + A
    for i in range (0 , m +1 ):
        A[i] = [B[i]] + A[i]
    matrix = numpy.zeros(shape=((round((numpy.shape(A))[0]/16) + 1)*16 ,
        (round((numpy.shape(A))[1]/32) + 1 )*32)).astype(numpy.float32)
    for i in range (m +1):
        for j in range (n + 1):
            matrix[i][j] = float(A[i][j])
    compute_cuda_simplex(matrix , x , slack)



n = 2
m = 3

C = [ -15 , -10 , 0 , 0 , 0 ]
B = [0 , 2 , 3 , 4]
A = [[1 , 0, 1 , 0 ,0 ], [0 , 1 , 0 , 1 , 0]  , [1 , 1 , 0 , 0 , 1]]

cuda_simple_simplex(A , B , C , ['x1' , 'x2' , 's1' ,'s2' ,'s3'] , ['s1' ,'s2' ,'s3'] , True)

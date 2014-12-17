import pycuda.driver as drv
import pycuda.tools
import pycuda.autoinit
import numpy
import numpy.linalg as la
from pycuda.compiler import SourceModule
from pycuda import gpuarray

# mod = SourceModule("""
# __global__ void multiply_them(float *dest, float *a, float *b)
# {
#   const int i = threadIdx.x;
#   dest[i] = a[i] * b[i];
# }
# """)

mod = SourceModule("""
__global__ void kernel1(float** simplex , float* teta , float* columnK , int k , int m){
    int idx = blockDim.x * blockIdx.x + threadIdx.x ;
    if(idx > m ) return;
    //float w = simplex[idx][k] ;
    /* copy the weights of entering index k */
    //columnK[idx] = w;
    //teta[idx] = simplex[idx][1]/w;
}

__global__ void kernel2(float** simplex , float* columnK ,  int k , int r){
    int idx = blockDim.x * blockIdx.x + threadIdx.x;
    __shared__ float w;
    /* Get the pivot element : simplex[r][k] in the shared memory */
    if(threadIdx.x == 0) w = columnK[r];
    __syncthreads();
    /*Update the line of leaving index r*/
    simplex[r][idx] = simplex[r][idx]/w;
}


__global__ void kernel3(float** simplex , float* columnK , int k , int r){
    int idx = blockDim.x + blockIdx.x + threadIdx.x;
    int jdx = blockIdx.y * blockDim.y + threadIdx.y;
    __shared__ float w[16];
    /* Get the column of entering index k in shared memory */
    if( threadIdx.y == 0 && threadIdx.x < 16)
    {
        w[threadIdx.x] = columnK[blockIdx.y * blockDim.y + threadIdx.x];
    }
    __syncthreads();
    /* Update the basis except the line r */

    if(idx == r) return;
    simplex[jdx][idx] = simplex[jdx][idx] - w[threadIdx.y]*simplex[r][idx];
}




__global__ void kernel4(float** simplex , float*  columnK , int k , int r){
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

# multiply_them = mod.get_function("multiply_them")
n = 2
m = 3
matrix = numpy.zeros(shape=(m+1 , n+1)).astype(numpy.float32)
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


# matrix[0][0] = 3
# matrix[0][1] = 2
# matrix[1][0] = 2
# matrix[1][1] = 2

# matrix[0][0] = 1
# matrix[0][1] = 0
# matrix[0][2] = 0
# matrix[1][0] = 0
# matrix[1][1] = 1
# matrix[1][2] = 0
# matrix[2][0] = 0
# matrix[2][1] = 0
# matrix[2][2] = 1
identity = numpy.identity(m + 1).astype(numpy.float32)

GaussJordan = numpy.zeros(shape=(m+1,n+1 + m + 1)).astype(numpy.float32)
columnK = numpy.zeros(shape=(m+1)).astype(numpy.float32)
teta = numpy.zeros(shape=(m+1)).astype(numpy.float32)

print identity
print GaussJordan
print matrix
GaussJordan_gpu = numpy

for i in range (0 , m + 1) :
    for j in range (0 , n + 1):
        GaussJordan[i][j] = matrix[i][j]
        if j < m+1 :
            GaussJordan[i ][j + n + 1] = identity[i][j]

# print "matrix \n" , matrix

# print "Identity \n" , identity

# print "GaussJordan \n" , GaussJordan


counter = 0
while(True):
    print "counter :" , counter
    print GaussJordan
    row = GaussJordan[0]
    minimum = 0
    i  = 0 
    # Find the index of entering variable k
    for item in row :
        i = i + 1
        if item < minimum :
            minimum = item
            k = i
    if minimum == 0 :
        print "solution is here\n" , GaussJordan
        break
    GaussJordan_gpu  = gpuarray.to_gpu( GaussJordan)
    teta_gpu = gpuarray.to_gpu(teta)
    columnK_gpu = gpuarray.to_gpu(columnK)

    kernel1 = mod.get_function("kernel1")
    h = int(((m+1) / 32) + 1)
    w = int(( (n + 1) / 16) + 1)
    kernel1(GaussJordan_gpu , teta_gpu ,  columnK_gpu , numpy.int32(k) , numpy.int32(m), block=(16 , 32 ,1 ) ,
     grid=(h , w  , 1))

    #find the index of leaving variable r
    print " teta " , teta

    print " gpu " , teta_gpu.get() 
    teta = teta_gpu.get()
    GaussJordan_gpu = GaussJordan_gpu.get()
    flag = False
    minimum 
    print "i :" , i
    print "k :" , k
    i = 0 
    for i in range (0 , m + 1):
        if GaussJordan_gpu[i][k] > 0 :
            Flag = True
            if not minimum:
                minimum = teta[i]
                r = i
            elif minimum > teta[i]:
                r = i
                minimum = teta[i]
    if not flag :
        print "unbounded"
        break

    kernel2 = mod.get_function("kernel2")
    h = int(((m+1) / 32) + 1)
    w = int(( (n + 1) / 16) + 1)
    kernel2(GaussJordan_gpu , columnK_gpu , numpy.int32(k), numpy.int32(r) , block=(16 , 32 , 1) , 
        grid=( h , w  , 1))
    h = int(((m+1) / 16) + 1)
    w = int(( (n + 1) / 32) + 1)

    kernel3 = mod.get_function("kernel3")

    kernel3(GaussJordan_gpu , columnK_gpu , numpy.int32(k), numpy.int32(r) , block=(32 , 16 , 1) ,
     grid=(h , w , 1))
    h = int(((m+1) / 32) + 1)
    w = int(( (n + 1) / 16) + 1)

    kernel4 = mod.get_function("kernel4")
    kernel4(GaussJordan_gpu , columnK_gpu , numpy.int32(k), numpy.int32(r) , block=(16 , 32 , 1) ,
     grid=(h , w , 1))

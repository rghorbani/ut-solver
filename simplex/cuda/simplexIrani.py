import pycuda.autoinit
import numpy
from pycuda.compiler import SourceModule
from pycuda import gpuarray, compiler


def compute_cuda_simplex(matrix ):
    print matrix
    matrix = numpy.array(matrix , copy=True , dtype=float)
    columnK = numpy.zeros(shape=(m+1)).astype(numpy.float32)
    teta = numpy.zeros(shape=(m+1)).astype(numpy.float32)
    SourceModule = ("""
    __global__ void kernel1(float simplex[((%(M)s/16)+1)*16][((%(N)s/32)+1)*32] , float* teta , float* columnK , int k ){
        int idx = blockDim.x * blockIdx.x + threadIdx.x ;
        float w = simplex[idx][k] ;
        /* copy the weights of entering index k */
        columnK[idx] = w;
        teta[idx] = simplex[idx][0]/w;
    }

    __global__ void kernel2(float simplex[((%(M)s/16)+1)*16][((%(N)s/32)+1)*32] , float* columnK ,  int k , int r){
        int idx = blockDim.y * blockIdx.y + threadIdx.y;
        __shared__ float w;
        /* Get the pivot element : simplex[r][k] in the shared memory */
        if(threadIdx.x == 0) w = columnK[r];
        __syncthreads();
        /*Update the line of leaving index r*/
        simplex[r][idx] = simplex[r][idx]/w;
    }


    __global__ void kernel3(float simplex[((%(M)s/16)+1)*16][((%(N)s/32)+1)*32] , float* columnK , int k , int r){
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




    __global__ void kernel4(float simplex[((%(M)s/16)+1)*16][((%(N)s/32)+1)*32] , float*  columnK , int k , int r){
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

    matrix_gpu  = gpuarray.to_gpu( matrix)
    teta_gpu = gpuarray.to_gpu(teta)
    columnK_gpu = gpuarray.to_gpu(columnK)
    counter = 0

    #width = GaussJordan.shape[0]
    #length = GaussJordan.shape[1]

    width = m
    length = n;
    print "width:", width
    print "length:",length
    print "matrix shape: ",matrix

    SourceModule_e = SourceModule%{
        'N' : length + width + 1,
        'M' : width + 1,

    }

    while(True):
        print "counter :" , counter
        counter+=1
        print matrix_gpu.get()
        row = matrix_gpu.get()[0]
        minimum = 0
        i  = 0 
        # Find the index of entering variable k
        for item in row :
            if item < minimum :
                minimum = item
                k = i
            i = i + 1
        if minimum == 0 :
            print "solution is here\n" , matrix_gpu.get()
            break

        mod = compiler.SourceModule(SourceModule_e)
        kernel1 = mod.get_function("kernel1")
        h = int(((m+1) / 32) + 1)
        w = int(( (n + 1) / 16) + 1)
        print "k : " , k
        kernel1(matrix_gpu , teta_gpu ,  columnK_gpu , numpy.int32(k) , block=(16 , 32 ,1 ) ,
         grid=(h , w  , 1))

        #find the index of leaving variable r
    #    print " teta " , teta

    #    print " gpu " , teta_gpu.get() 
    #    matrix_gpu = matrix_gpu.get()
        print "kernel1 out GausJordan\n" ,matrix_gpu.get()

        flag = False
        minimum = -1
        print "i :" , i
        print "k :" , k
        print "teta_gpu:\n", teta_gpu.get()
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
        print "kernel1 out GausJordan\n" ,matrix_gpu.get()
        h = int(((m+1) / 32) + 1)
        w = int(( (n + 1) / 16) + 1)
        kernel2(matrix_gpu , columnK_gpu , numpy.int32(k), numpy.int32(r) , block=(16 , 32 , 1) , 
            grid=( h , w  , 1))
    #    h = int(((m+1) / 16) + 1)
    #    w = int(( (n + 1) / 32) + 1)
        h = int(((m+1) / 32) + 1)
        w = int(( (n + 1) / 16) + 1)
        print "r :" , r
        print "kernel2 out GausJordan\n" ,matrix_gpu.get()
        kernel3 = mod.get_function("kernel3")

        kernel3(matrix_gpu , columnK_gpu , numpy.int32(k), numpy.int32(r) , block=(16 , 32 , 1) ,
         grid=(h , w , 1))
        h = int(((m+1) / 32) + 1)
        w = int(( (n + 1) / 16) + 1)
        print "kernel3 out GausJordan\n" ,matrix_gpu.get()
        kernel4 = mod.get_function("kernel4")
        kernel4(matrix_gpu , columnK_gpu , numpy.int32(k), numpy.int32(r) , block=(16 , 32 , 1) ,
         grid=(h , w , 1))
        print "kernel4 out GausJordan\n" ,matrix_gpu.get()
        if counter>1:
            break



def uni_phase_simplex(A , B , C):
    m = len(A)
    if m <= 0 :
        return
    n = len(A[0])
    B = [0] + B
    A = [C] + A
    for i in range (0 , m +1 ):
        print B[i]
        A[i] = [B[i]] + A[i]

    print "glhglkh" ,A    
    compute_cuda_simplex(A)

def cuda_simplex(+):
#def find_feasible_point(A, B, C, virtuals_indices, slacks_indices):
    feasible_point = numpy.zeros(len(C))

    if len(virtuals_indices) == 0 :
        uni_phase_simplex(A,B,C)
    else:
        C_phase_1 = [0] * (len(C)-len(virtuals_constraints_num))
        basics = [0] * (len(B)-1)
        for i in range(len(virtuals_indices)):
            C_phase_1.append(-1)
        print (" C=  " , C_phase_1)
        for i in range(len(virtuals_constraints_num)):
            for j in range(len(C)):
                C_phase_1[j] +=  A[virtuals_constraints_num[i]-1][j]
            print (" C=  " , C_phase_1)
            B[0] += B[virtuals_constraints_num[i]]
            basics [virtuals_constraints_num[i]-1] = virtuals_indices[i]

        for i in range(len(slacks_constraint_num)):
            if(basics[slacks_constraint_num[i]-1] == 0 ):
                basics[slacks_constraint_num[i]-1] = slacks_indices[i]
        print ("Normilized Phase#1")

        for i in range(len(C_phase_1)):
            C_phase_1[i] *= -1
        print "Basic:",basics
        print "constraint:",C_phase_1
        print "B:",B
        uni_phase_simplex(A,B,C_phase_1)

        if (C_phase_1[len(C_phase_1)-1] != 0 ):
            print ("not Find feasible region")
        else:
            basics1_int = basics
            #Phase#2
            C.append(0)
            print ("Pashe #2")
            print_matrix(A)
            print ('c',C)
            print ('basics',basics1_int)
            print('b',B)
            for i in range (len(basics1_int)):
                #print ('basic is ' ,A[i][basics1_int[i]-1])
                if(C[basics1_int[i]-1] != 0):
                    piv = C[basics1_int[i]-1] / A[i][basics1_int[i]-1]
                else:
                    piv = 0 ;
                #print ('pivot' , piv)
                temp = []
                for k in range(len(A[i])):
                    temp.append( A[i][k] * piv)
                #print ('temp' , temp)
                for p in range(len(A[i])):
                    C[p] -= temp[p]
                #print ('##### C ' , c) 
                for j in range (len(basics1_int)):
                   #print ('j' , j)
                   if (j!=i):
                       if(A[i][basics1_int[i]-1] != 0):
                           piv = A[j][basics1_int[i]-1] / A[i][basics1_int[i]-1]
                       else:
                           piv = 0 ;
                       #print ('pivot' , piv)
                       temp = []
                       for k in range(len(A[i])):
                           temp.append( A[i][k] * piv)
                       #print ('temp' , temp)
                       for p in range(len(A[i])):
                           A[j][p] -= temp[p]
                #print_matrix (A)
            print ('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
            print ('normilized Phase#2')
            #print_matrix(A)
            #print (c)
            b2 = column(A,len(A[0])-1)
            c_temp = C[len(C)-1]
            b2.insert(0,c_temp)
            C.pop(len(C)-1)
            A2 = pop_column(A,len(A[0])-1)
            print_matrix (A2)
            print ( C)
            print ( b2 )
            print (basics1_int)

            uni_phase_simplex(A,B,C)
        return


n = 2
m = 3

#C = -1 * [ 15 , 10]
#B = [ 2 , 3 , 4]
#A = [[1 , 0], [0 , 1]  , [1 , 1]]
#x = ['x1','x2']
#virtuals_indices=[]
#virtuals_constraints_num=[]
#slacks_constraint_num=[1,2,3]
#slacks_indices=[3 , 4, 5]

A = [[1,1,-1,0,0,1,0],[-1,1,0,-1,0,0,1],[0,1,0,0,1,0,0]]
C = [-1,2,0,0,0,0,0]
B = [0,2,1,3]
x = ['x1','x2','x3','x4','x5','x6','x7']
virtuals_indices=[6 , 7]
virtuals_constraints_num=[1, 2]
slacks_constraint_num=[1,2,3]
slacks_indices=[3 , 4, 5]


#find_feasible_point(A, B, C, virtuals_indices, slacks_indices)
cuda_simplex(A,B,C,virtuals_constraints_num, virtuals_indices, slacks_constraint_num , slacks_indices )
#uni_phase_simplex(A,B,C)
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

#print "booogh" , matrix 

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

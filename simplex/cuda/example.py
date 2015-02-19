import simplex
import numpy

A = numpy.array([
     [1,0,1,0,0]
    ,[0,1,0,1,0]
    ,[1,1,0,0,1]
    ])
C = numpy.array([15,10,0,0,0])
B = numpy.array([0,2,3,4])
# x      y      s1     s2     s3     s4
x = numpy.array(['x1','x2','s1','s2','s3'])
virtuals_indices=numpy.array([])
virtuals_constraints_num=numpy.array([])
slacks_constraint_num=numpy.array([1,2,3])
slacks_indices=numpy.array([3 , 4 ,5])


simplex.log("Starting")
#find_feasible_point(A, B, C, virtuals_indices, slacks_indices)
result = simplex.find_feasible_point(A,B,C,virtuals_constraints_num, virtuals_indices, slacks_constraint_num , slacks_indices , False)
simplex.log( "result \n\n" + str(result))

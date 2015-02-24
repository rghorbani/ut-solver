import simplex
import numpy

# A = numpy.array([
#      [1,0,1,0,0]
#     ,[0,1,0,1,0]
#     ,[1,1,0,0,1]
#     ])
# C = numpy.array([15,10,0,0,0])
# B = numpy.array([0,2,3,4])
# # x      y      s1     s2     s3     s4
# x = numpy.array(['x1','x2','s1','s2','s3'])
# virtuals_indices=numpy.array([])
# virtuals_constraints_num=numpy.array([])
# slacks_constraint_num=numpy.array([1,2,3])
# slacks_indices=numpy.array([3 , 4 ,5])
C = numpy.loadtxt("output/c")
B = numpy.loadtxt("output/b")
A = numpy.loadtxt("output/a")


# virtuals_indices=numpy.loadtxt("output/virtual_constraint")
virtuals_constraints_num=numpy.array("output/virtual_constraint")

A_added_virtuals= numpy.zeros(shape=(len(A),(len(A[0]) + len(virtual_constraint))))
for i in len(A_added_virtuals):
	for j in len(A[0]):
		A_added_virtuals[i][j] = A[i][j]

virtuals_indices = []
k = 0 
for i in virtual_constraint:
	A_added_virtuals[i-1][k + len(A[0])] = -1
	k++
	virtuals_indices = virtuals_indices + [k + len(A[0])]

slacks_constraint_num=numpy.loadtxt("output/slack_constraints")
slacks_indices=numpy.loadtxt("output/slack_indexes")



simplex.log("Starting")
print " A :" , len(A) , len(A[0])
print " B :" , len(B) 
print " C :" , len(C) 

#find_feasible_point(A, B, C, virtuals_indices, slacks_indices)
result = simplex.find_feasible_point(A,B,C,virtuals_constraints_num, virtuals_indices, 
	slacks_constraint_num , slacks_indices , False)
simplex.log( "result \n\n" + str(result))

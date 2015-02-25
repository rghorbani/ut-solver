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
def solving_cuda():
	C = numpy.loadtxt("output/c")
	B = numpy.loadtxt("output/b")
	A = numpy.loadtxt("output/a")
	# variables = numpy.loadtxt("output/varable_names")

	# virtuals_indices=numpy.loadtxt("output/virtual_constraint")
	virtuals_constraints_num = numpy.loadtxt("output/virtual_constraint" , ndmin=1)
	A_added_virtuals = numpy.zeros(shape=(len(A),(len(A[0]) + len(virtuals_constraints_num))))
	for i in range(len(A_added_virtuals)):
		for j in range(len(A[0])):
			A_added_virtuals[i][j] = A[i][j]

	virtuals_indices = []
	k = 0 
	for i in range(len(virtuals_constraints_num)):
		# print " a :" , virtuals_constraints_num [i-1]
		# print " b :" , k + len(A[0])
		# print "len :" , len(A_added_virtuals)
		# print "len :" , len(A_added_virtuals[0])
		A_added_virtuals[virtuals_constraints_num [i-1] -1  ][k + len(A[0])] = -1
		k += 1
		virtuals_indices = virtuals_indices + [k + len(A[0])]

	slacks_constraint_num = numpy.loadtxt("output/slack_constraints")
	slacks_indices = numpy.loadtxt("output/slack_indexes")
	# print "slack_indexes" , slacks_indices
	# print "slacks_constraint_num" , slacks_constraint_num 
	# print "virtuals_indices" , virtuals_indices
	# print "virtuals_constraints_num" , virtuals_constraints_num
	B_revised = numpy.zeros(shape=(len(B) +1))
	C_revised = numpy.zeros(shape=(len(A_added_virtuals[0])))
	for i in range (1 ,len(B_revised)):
		B_revised[i] = B[i-1]
	for i in range(len(C)):
		C_revised[i] = C[i]
	# print " A :" , len(A) , len(A[0]) 
	# print " B :" , len(B) 
	# print " B_revised :" , len(B_revised) 
	# print " C :" , len(C)
	# print "boogh"
	# print "A_added_virtuals" , A_added_virtuals
	# print virtuals_constraints_num 
	# print "boogh"
	# print virtuals_indices

	#find_feasible_point(A, B, C, virtuals_indices, slacks_indices)
	result = simplex.find_feasible_point(A_added_virtuals ,B_revised,C_revised,
		virtuals_constraints_num, virtuals_indices, 
		slacks_constraint_num , slacks_indices , True)
	# simplex.log( "variables "  + str(variabl))
	simplex.log( "result \n\n" + str(result))
	return result
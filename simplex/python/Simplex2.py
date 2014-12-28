import string
import re

INF = 999999999
class Simplex:

	def printItself(self):
		print ("***")
		s = [[str(e) for e in row] for row in self.simplex]
		lens = [max(map(len, col)) for col in zip(*s)]
		fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
		table = [fmt.format(*row) for row in s]
		print ('\n'.join(table))
		print ("***")
  
	def __init__(self,A,C,B,x,basics ):
		self.simplex = []
		for i in range(len(A)+1):
			if i == 0:
				C.append(B[0])
				self.simplex.append(C)
			else:
				A[i-1].append(B[i])
				self.simplex.append(A[i-1])

	def find_pivot_column_index_max(self,lenC):
		min_value = min(self.simplex[0]);
		min_value_index = self.simplex[0][0:lenC].index(min(self.simplex[0][0:lenC]));
		if(min_value >= 0):
			return -1
		else:
			return min_value_index

	def find_pivot_column_index_min(self,lenC):
		max_value = max(self.simplex[0]);
		max_value_index = self.simplex[0][0:lenC].index(max(self.simplex[0][0:lenC]));
		if(max_value <= 0):
			return -1
		else:
			return max_value_index

	def find_pivot_row_index(self,n,m,pivot_column_index):
		rate = []
		for i in range(1 , m+1):
			if (self.simplex[i][pivot_column_index] != 0):
				rate.append(self.simplex[i][n] / self.simplex[i][pivot_column_index])
			else:
				if(self.simplex[i][n] < 0):
					rate.append(-INF)
				else:
					rate.append(+INF)
		is_has_positive = len([x for x in rate if( x > 0  and  x!= +INF) ])
		if(is_has_positive):
			positive_min_value =  min(el for el in rate if el > 0)
			positive_min_value_index = rate.index(min(el for el in rate if el > 0))
			return positive_min_value_index + 1
		else:
			return -1

	def gauss_operations(self,n,m,pivot_column_index,pivot_row_index):
		pivot = self.simplex[pivot_row_index][pivot_column_index]
		if pivot != 0:
			for i in range (n+1):
				self.simplex[pivot_row_index][i] = round( self.simplex[pivot_row_index][i] / pivot , 5 )
		   
			for i in range(m+1):
				pivot = self.simplex[i][pivot_column_index]
				for j in range(n+1):
					if(i != pivot_row_index):
						self.simplex[i][j] =round ( self.simplex[i][j] - ( pivot * self.simplex[pivot_row_index][j] ) ,5)
		self.printItself() 


def print_matrix(m):
	print ("***")
	s = [[str(e) for e in row] for row in m]
	lens = [max(map(len, col)) for col in zip(*s)]
	fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
	table = [fmt.format(*row) for row in s]
	print ('\n'.join(table))
	print ("***")

def simple_simplex(A,c,b,x,basics,is_max):
    n = len(c)
    m = len(A)
    s = Simplex(A,c,b,x,basics)
    s.printItself() 
    while(True):
        print (basics)
        if(is_max):
            pivot_column_index = s.find_pivot_column_index_max(n)
        else:
            pivot_column_index = s.find_pivot_column_index_min(n)
        if (pivot_column_index == -1):
            break ;
        pivot_row_index = s.find_pivot_row_index(n,m,pivot_column_index)
        print (pivot_column_index)
        print (pivot_row_index)
        basics[pivot_row_index-1] = x[pivot_column_index]
		#print pivot_row_index
        if(pivot_row_index == -1):
            print ("No move to Feasible Region")
            break ;
        s.gauss_operations(n,m,pivot_column_index,pivot_row_index)
    print("is Optimum point")
        #is Optimum Point


def phase2_simplex(A,c,b,x,basics,is_max):
    n = len(c)
    m = len(A)
    s2 = Simplex(A,c,b,x,basics)
    s2.printItself() 
    while(True):
        print (basics)
        if(is_max):
            pivot_column_index = s2.find_pivot_column_index_max(n)
        else:
            pivot_column_index = s2.find_pivot_column_index_min(n)
        if (pivot_column_index == -1):
            break ;
        pivot_row_index = s2.find_pivot_row_index(n,m,pivot_column_index)
        #print "@@@@@@@@@@@@"
        print (pivot_column_index)
        print (pivot_row_index)
        #print x
        #print "!!!!!!!!!!!!!"
        #print basics
        basics[pivot_row_index-1] = x[pivot_column_index]
        
		#print pivot_row_index
        if(pivot_row_index == -1):
            print ("No move to Feasible Region")
            break ;
        s2.gauss_operations(n,m,pivot_column_index,pivot_row_index)
    print("is Optimum point")
        #is Optimum Point

def column(matrix, i):
    return [row[i] for row in matrix]
def pop_column(matrix, j):
    for i in range(len(matrix)):
        matrix[i].pop(j)
    return matrix
def two_phase_simplex(A,c,b,x,slags,slag_constraint_number,virtuals , virtual_constraint_number ,is_max ):
    c1 = [0] * (len(c)-len(virtuals))
    basics1 = [0] * (len(b)-1)
    for i in range(len(virtuals)):
        c1.append(-1)
    #print (" c1=  " , c1)
    for i in range(len(virtual_constraint_number)):
        for j in range(len(c1)):
            c1 [j] +=  A[virtual_constraint_number[i]-1][j]
        #print (" c1=  " , c1)
        b[0] += b[virtual_constraint_number[i]]
        basics1 [virtual_constraint_number[i]-1] = virtuals[i]

    for i in range(len(slag_constraint_number)):
        if(basics1[slag_constraint_number[i]-1] == 0 ):
            basics1[slag_constraint_number[i]-1] = slags[i]
    print ("Normilized Phase#1")
    print_matrix(A)
    print ("c1=  " , c1)
    print ("b =  " , b)
    print ("basics1=  " , basics1)
    simple_simplex(A,c1,b,x,basics1 , 0 )


    if (c1[len(c1)-1] != 0 ):
        print ("not Find feasible region")
    else:
        print ('out_basic', basics1)
        basics1_str = [y[1:] for y in basics1]
        print "x :" , x
        print ('out ', basics1_str)
        
        basics1_int = [int(s) for s in basics1_str if s.isdigit()]

        #Phase#2
        c.append(0)
        print ("Pashe #2")
        print_matrix(A)
        print ('c',c)
        print ('basics',basics1_int)
        print('b',b)
        for i in range (len(basics1_int)):
            #print ('basic is ' ,A[i][basics1_int[i]-1])
            if(c[basics1_int[i]-1] != 0):
                piv = c[basics1_int[i]-1] / A[i][basics1_int[i]-1]
            else:
                piv = 0 ;
            #print ('pivot' , piv)
            temp = []
            for k in range(len(A[i])):
                temp.append( A[i][k] * piv)
            #print ('temp' , temp)
            for p in range(len(A[i])):
                c[p] -= temp[p]
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
        print ('normalized Phase#2')
        #print_matrix(A)
        #print (c)
        b2 = column(A,len(A[0])-1)
        c_temp = c[len(c)-1]
        b2.insert(0,c_temp)
        c.pop(len(c)-1)
        A2 = pop_column(A,len(A[0])-1)
        print_matrix (A2)
        print ( c)
        print ( b2 )
        print (basics1_int)

        phase2_simplex(A2,c,b2,x,basics1_int,is_max)
               


#A = [[6,4,0,1,0,0,0],[1,2,0,1,0,0,0],[-1,1,0,7,1,0,0],[0,1,6,9,0,0,1]]
#c = [5,-4,0,-3,0,0,0]
#b = [0,24,6,4,2]
#x = ['x1','x2','x3','x4','x5','x6','x7']

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
    two_phase_simplex(A,c,b,x,slags,slag_constraint_number,virtuals, virtual_constraint_number ,is_max )
else:
    slags = ['x3','x4','x5','x6','x7']
    simple_simplex(A,c,b,x,slags,is_max )
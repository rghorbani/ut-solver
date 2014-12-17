import string    

INF = 999999999
class Dual:

	def __init__(self,A,c,b):	
		self.dual = []
		for i in range(len(A[0])+1):
			if i == 0:
				self.dual.append(b)
			else:
				temp = []
				for j in range (len(A)):
					temp.append(A[j][i-1])
				temp.append(c[i-1])
				self.dual.append(temp)
#=====================================================
	def printItself(self):

		print ("***")
		s = [[str(e) for e in row] for row in self.dual]
		lens = [max(map(len, col)) for col in zip(*s)]
		fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
		table = [fmt.format(*row) for row in s]
		print ('\n'.join(table))
		print ("***")
#=====================================================
	def find_pivot_row_index(self):
		last = len(self.dual[0])-1
		min_value = min(self.dual[last])
		min_value_index = self.dual[last][1:(len(self.dual)-1)].index(min_value)
		if(min_value >= 0):
			return -1
		else:
			return min_value_index + 1
#=====================================================
	def find_pivot_column_index(self,pivot_row_index):
		rate = []
		for i in range(0 , len(self.dual[0])-1):
			if self.dual[pivot_row_index][i] < 0:
				if (self.dual[pivot_row_index][i] != 0):
					rate.append(self.dual[0][i] / self.dual[pivot_row_index][i])
				else:
					if(self.dual[0][i] < 0):
						rate.append(-INF)
					else:
						rate.append(+INF)
		is_has_positive = len([x for x in rate if( x > 0  and  x!= +INF) ])
		if(is_has_positive):
			positive_min_value =  min(el for el in rate if el > 0)
			positive_min_value_index = rate.index(min(el for el in rate if el > 0))
			return positive_min_value_index
		else:
			return -1
#=====================================================
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


#=====================================================
def dual_simplex():

    A = [[1,2,-3,0],[4,5,0,6],[5,6,7,0]]
    c = [-1,-2,-5,-4]
    b = [0,10,20,30]
    is_max=1

    m = len(c)
    n = len(A)
    s = Dual(A,c,b)
    s.printItself() 

    while(True):
		pivot_row_index = s.find_pivot_row_index()
		if (pivot_row_index == -1):
			break ;
		pivot_column_index = s.find_pivot_column_index(pivot_row_index)
		print pivot_column_index
		if(pivot_column_index == -1):
			print ("No Optimum Answer!")
			break
		s.gauss_operations(m,n,pivot_column_index,pivot_row_index)

    print("is optimum point")
        #is Optimum Point

#simple_simplex()	
dual_simplex()
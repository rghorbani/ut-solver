
INF = 999999999


class Simplex:

    def print_it_self(self):
        print ("***")
        s = [[str(e) for e in row] for row in self.simplex]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print ('\n'.join(table))
        print ("***")
  
    def __init__(self, a_matrix, c_matrix, b_matrix):
        self.simplex = []
        for i in range(len(a_matrix) + 1):
            if i == 0:
                c_matrix.append(b_matrix[0])
                self.simplex.append(c_matrix)
            else:
                a_matrix[i - 1].append(b_matrix[i])
                self.simplex.append(a_matrix[i - 1])

    def find_pivot_column_index(self, len_c):
        min_value = min(self.simplex[0])
        min_value_index = self.simplex[0][0:len_c].index(min(self.simplex[0][0:len_c]))
        if min_value >= 0:
            return -1
        else:
            return min_value_index

    def find_pivot_row_index(self, n, m, pivot_column_index):
        rate = []
        for i in range(1, m + 1):
            if self.simplex[i][pivot_column_index] != 0:
                rate.append(self.simplex[i][n] / self.simplex[i][pivot_column_index])
            else:
                if self.simplex[i][n] < 0:
                    rate.append(-INF)
                else:
                    rate.append(+INF)
        is_has_positive = len([x for x in rate if(x > 0 and x != +INF)])
        if is_has_positive:
            # positive_min_value = min(el for el in rate if el > 0)
            positive_min_value_index = rate.index(min(el for el in rate if el > 0))
            return positive_min_value_index + 1
        else:
            return -1

    def gauss_operations(self, n, m, pivot_column_index, pivot_row_index):
        pivot = self.simplex[pivot_row_index][pivot_column_index]
        if pivot != 0:
            for i in range(n + 1):
                self.simplex[pivot_row_index][i] = self.simplex[pivot_row_index][i] / pivot
           
            for i in range(m + 1):
                pivot = self.simplex[i][pivot_column_index]
                for j in range(n + 1):
                    if i != pivot_row_index:
                        self.simplex[i][j] = self.simplex[i][j] - (pivot * self.simplex[pivot_row_index][j])
        # self.print_it_self()

    def result(self, n):
        return self.simplex[0][n]


def simple_simplex(a, b, c):
    
    # A = [[6,4,1,0,0,0],[1,2,0,1,0,0],[-1,1,0,0,1,0],[0,1,0,0,0,1]]
    # c = [-5,-4,0,0,0,0]
    # b = [0,24,6,1,2]
    # A = [[6,4,1,0,0,0],[1,2,0,1,0,0],[-1,1,0,0,1,0],[0,1,0,0,0,1]]
    # c = [-5,-4,0,0,0,0]
    # b = [0,24,6,1,2]
    n = len(c)
    m = len(a)
    s = Simplex(a, c, b)
    # s.print_it_self()

    while True:
        pivot_column_index = s.find_pivot_column_index(n)
        if pivot_column_index == -1:
            break
        pivot_row_index = s.find_pivot_row_index(n, m, pivot_column_index)
        # print pivot_row_index
        if pivot_row_index == -1:
            print ("No move to Feasible Region")
            break
        s.gauss_operations(n, m, pivot_column_index, pivot_row_index)

    # print("is Optimum point")
    return s.result(n)
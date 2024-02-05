import numpy as np

class Matrix:
    def __init__(self,matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[1])

    def get_neighbours(self,row,column):
        lst = []
        for i in range(max(0,row - 1), min(self.rows, row + 2)):
            for j in range(max(0,column - 1), min(self.columns, column + 2)):
                lst.append(self.matrix[i][j])
        return lst
    def get_max(self):
        result = np.zeros((self.rows,self.columns), dtype=int)
        for i in range(self.rows):
            for j in range(self.columns):
                result[i][j] = max(self.get_neighbours(i,j))
        return result


with open('Question 3\input_question_3', 'r') as f:
    input_matrix = []
    for line in f.readlines():
        input = line.split(' ')
        input = np.array(input).astype('int').tolist()
        input_matrix.append(input)

matrix = Matrix(input_matrix)
max = matrix.get_max()
result = ""
for i in max:
    for j in i:
        result += "{} ".format(j)
    result += "\n"

f = open("Question 3\output_question_3.txt", "a")
f.write(result)
f.close()


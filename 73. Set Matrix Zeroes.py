class Solution(object):
    def setZeroes(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        Row = [-1] * row
        Col = [-1] * col
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    Row[i] = 0
                    Col[j] = 0
        for i in range(row):
            for j in range(col):
                if Row[i] == 0 or Col[j] == 0:
                    matrix[i][j] = 0

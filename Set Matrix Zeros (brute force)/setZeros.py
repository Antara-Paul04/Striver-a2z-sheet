class Solution(object):
    def markRow(self, i, matrix, n):
        for j in range(n):
            if matrix[i][j] != 0:
                matrix[i][j] = float('inf') 

    def markColumn(self, j, matrix, m):
        for i in range(m):
            if matrix[i][j] != 0:
                matrix[i][j] = float('inf') 

    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    self.markRow(i, matrix, n)
                    self.markColumn(j, matrix, m)

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == float('inf') :
                    matrix[i][j] = 0

        return matrix

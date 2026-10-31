class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows2zero, cols2zero = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows2zero.add(i)
                    cols2zero.add(j)
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rows2zero or j in cols2zero:
                    matrix[i][j] = 0

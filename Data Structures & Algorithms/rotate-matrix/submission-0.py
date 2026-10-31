class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for c in range(len(matrix)):
            for r in range(c + 1):
                temp = matrix[c][r]
                matrix[c][r] = matrix[r][c]
                matrix[r][c] = temp
                
        for row in matrix:
            row.reverse()
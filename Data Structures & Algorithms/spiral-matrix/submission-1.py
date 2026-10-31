class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        array = []

        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        # right (till right) -> down (till bottom) -> left (till left) -> up (till top)
        while top <= bottom and left <= right:
            # ---RIGHT---
            for i in range(left, right + 1):
                array.append(matrix[top][i])
            top += 1

            # ---DOWN---
            for i in range(top, bottom + 1):
                array.append(matrix[i][right])
            right -= 1

            # ---LEFT---
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    array.append(matrix[bottom][i])
                bottom -= 1

            # ---UP---
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    array.append(matrix[i][left])
                left += 1
        return array
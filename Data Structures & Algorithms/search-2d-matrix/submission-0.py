class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # start with top right
        # too small -> down
        # too big -> left

        cur_r, cur_c = len(matrix) - 1, 0

        while cur_r >= 0 and cur_c <= len(matrix[0]) - 1:
            if matrix[cur_r][cur_c] == target:
                return True
            # TOO SMALL
            elif matrix[cur_r][cur_c] < target:
                cur_c += 1
            # TOO BIG
            elif matrix[cur_r][cur_c] > target:
                cur_r -= 1

        return False
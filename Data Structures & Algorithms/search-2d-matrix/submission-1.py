class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # start with top right
        # too small -> down
        # too big -> left
        for row in matrix:
            lo, hi = 0, len(row) - 1

            while lo <= hi:
                mid = (lo + hi) // 2

                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return False
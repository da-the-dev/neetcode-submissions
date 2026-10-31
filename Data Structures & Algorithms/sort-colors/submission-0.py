class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        reds = 0
        whites = 0
        blues = 0
        for n in nums:
            if n == 0:
                reds += 1
            elif n == 1:
                whites += 1
            elif n == 2:
                blues += 1
        
        nums[:] = ([0] * reds + [1] * whites + [2] * blues)
        
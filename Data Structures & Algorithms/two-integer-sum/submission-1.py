class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summ = {}

        for i, n in enumerate(nums):
            summ[n] = i

        
        for i, n in enumerate(nums):
            if (neg := target - n) in summ.keys() and summ[neg] != i:
                return [i, summ[target - n]]
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        summ = {}

        for i, n in enumerate(numbers):
            summ[n] = i

        
        for i, n in enumerate(numbers):
            if (neg := target - n) in summ.keys() and summ[neg] != i:
                return [i + 1, summ[target - n] + 1]
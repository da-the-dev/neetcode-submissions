class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        width = 1
        temp = [None] * n

        while width < n:
            for left in range(0, n, 2 * width):
                mid = min(left + width, n)
                right = min(left + 2 * width, n)

                i = left
                j = mid
                k = left

                # Merge two sorted ranges:
                # arr[left:mid] and arr[mid:right]
                while i < mid and j < right:
                    if nums[i] <= nums[j]:
                        temp[k] = nums[i]
                        i += 1
                    else:
                        temp[k] = nums[j]
                        j += 1
                    k += 1

                while i < mid:
                    temp[k] = nums[i]
                    i += 1
                    k += 1

                while j < right:
                    temp[k] = nums[j]
                    j += 1
                    k += 1

            # Copy the merged pass back into nums
            nums[:] = temp[:]

            width *= 2

        return nums
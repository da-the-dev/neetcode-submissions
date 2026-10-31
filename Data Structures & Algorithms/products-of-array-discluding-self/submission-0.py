class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = [1]
        right_products = [1]

        left_running_product = 1
        for n in nums[:-1]:
            left_running_product *= n
            left_products.append(left_running_product) 

        right_running_product = 1
        for n in nums[::-1][:-1]:
            right_running_product *= n
            right_products.append(right_running_product) 
            
        return [l * r for l, r in zip(left_products, right_products[::-1])]
            
            
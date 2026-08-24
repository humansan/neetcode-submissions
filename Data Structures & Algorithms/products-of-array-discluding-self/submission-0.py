class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        cur_product = 1
        result = []

        for i in range(len(nums)):
            result.append(cur_product)
            cur_product *= nums[i]
        
        cur_product = 1

        for i in range(len(nums)-1, -1, -1):
            result[i] *= cur_product
            cur_product *= nums[i]
        
        return result

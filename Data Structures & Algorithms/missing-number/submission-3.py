class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        xor_nums = list(range(len(nums) + 1)) + nums
        running_xor = 0

        for i in range(len(xor_nums)):
            running_xor ^= xor_nums[i]
        
        return running_xor
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        target = len(nums) * (len(nums) + 1) // 2

        for num in nums:
            target -= num

        return target
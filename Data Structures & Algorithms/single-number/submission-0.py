class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        running_xor = 0

        for num in nums:
            running_xor ^= num

        return running_xor
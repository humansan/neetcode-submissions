class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        max_len = 0

        for num in nums:
            if num - 1 not in num_set:
                l = 1
                while num + l in num_set:
                    l += 1
                max_len = max(l, max_len)
        
        return max_len
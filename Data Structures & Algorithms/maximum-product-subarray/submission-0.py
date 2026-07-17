class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curmax = 1
        curmin = 1
        truemax = nums[0]

        for num in nums:
            if num < 0: 
                curmax, curmin = curmin, curmax

            curmax = max(num, curmax*num)
            curmin = min(num, curmin*num)
            truemax = max(truemax, curmax)
        
        return truemax

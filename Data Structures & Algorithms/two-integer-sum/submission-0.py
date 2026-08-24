class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # iterate through array
        # check if complement exists in map from previous substring
        # store the index so it can be checked in future numbers
        complements = {}

        for i, num in enumerate(nums):
            if target - num in complements:
                return [complements[target - num], i]
                
            complements[num] = i

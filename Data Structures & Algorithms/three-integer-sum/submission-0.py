class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # sort
        # iterate left pointer
        # skip if left is equal to previous left
        # create 2 pointer within rest of substring
        # if sum is > 0, move right inward
        # if sum is < 0, move left rightward
        # if sum is 0, move left, and then skip while duplicate

        nums.sort()
        solutions = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            subtarget = -nums[i]

            while l < r:
                if nums[l] + nums[r] > subtarget:
                    r -= 1
                elif nums[l] + nums[r] < subtarget:
                    l += 1
                else:
                    solutions.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        
        return solutions




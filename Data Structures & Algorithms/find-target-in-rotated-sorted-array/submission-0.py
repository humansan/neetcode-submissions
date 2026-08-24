class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # check middle against target
        # find sorted section
            # if mid > r, sorted is left section else right section
            # check if target would be in bounds of sorted section
            # otherwise set l/r to other section
            # repeat

        l, r = 0, len(nums)-1
        
        while l <= r: # mid can be = l = r
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > nums[r]: # sorted is left section
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_of_nums = sum(nums)
        if sum_of_nums % 2:
            return False

        target = sum_of_nums // 2
        possible_sums = set([0])

        for num in nums:
            new_sums = set()
            for possible in possible_sums:
                if num + possible == target:
                    return True
                if num + possible < target:
                    new_sums.add(num + possible)
                    
                new_sums.add(possible)

            possible_sums = new_sums
        
        print(target)
        print(sum_of_nums)
        print(possible_sums)
        
        return False

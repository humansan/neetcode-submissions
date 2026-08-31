class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[0])

        prevEnd = intervals[0][1]

        # how many intervals we need to remove
        counter = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < prevEnd:
                # there is a conflict between a pair of adjacent intervals
                # keep the one that ends earlier
                prevEnd = min(intervals[i][1], prevEnd)
                counter += 1
            else:
                # there is no conflict, prev end just needs to be updated
                prevEnd = intervals[i][1]
            
        return counter
        
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        for i in range(len(intervals)):
            start, end = intervals[i]
            if newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > end:
                res.append(intervals[i])
            else:
                # overlap
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)
        
        #  if we reach here it means the new interval goes at the end
        # either all the other intervals come before the new interval
        # or the last interval conflicts with the new interval, 
        # in which case the last interval is not added and the loop exits afterward
            # either way we have to add the new interval here, (either it's going after the last interval, or it's overlapping the last interval and will go in its place since the start/end of new interval now supersedes the last interval
        res.append(newInterval)
        return res
        



            
# 1-2 4-5 7-8

# inserting 3-4

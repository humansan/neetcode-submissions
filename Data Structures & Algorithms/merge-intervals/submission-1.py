class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x: x[0])
        

        i = 0
        runs = len(intervals)

        while(i < runs-1):
            if intervals[i][0] <= intervals[i+1][1] and intervals[i][1] >= intervals[i+1][0]:
                # there is a overlap
                intervals[i][0] = min(intervals[i][0], intervals[i+1][0])
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.pop(i+1)
                runs -= 1
            else:
                i+=1
        
        return intervals


# 1-3 1-5 6-7
            

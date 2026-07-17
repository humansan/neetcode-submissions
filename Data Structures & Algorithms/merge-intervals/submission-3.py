class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x: x[0])
        
        results = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= results[-1][1]:
                results[-1][1] = max(intervals[i][1], results[-1][1])
            else:
                results.append(intervals[i])

        return results            

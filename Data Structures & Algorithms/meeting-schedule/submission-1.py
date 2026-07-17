"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
            
        interval_heap = [(i.start,i.end) for i in intervals]

        heapq.heapify(interval_heap)

        first = heapq.heappop(interval_heap)
        while interval_heap:
            second = heapq.heappop(interval_heap)
            if first[1] > second[0]:
                return False
            first = second
            
        
        return True
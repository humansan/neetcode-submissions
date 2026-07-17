"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        cur_meetings = 0
        min_rooms = 0

        start = [i.start for i in intervals]
        end = [i.end for i in intervals]
        start.sort()
        end.sort()

        end_pointer = 0

        for s in start:
            while s >= end[end_pointer]:
                cur_meetings -= 1
                end_pointer += 1
            
            cur_meetings += 1
            min_rooms = max(min_rooms, cur_meetings)
        
        return min_rooms
            


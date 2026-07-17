"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        current_meetings = []
        min_rooms = 0

        intervals.sort(key = lambda i: i.start)

        for i in range(0, len(intervals)):
            meeting = intervals[i]

            for om in current_meetings:
                if meeting.start >= om.end:
                    current_meetings.remove(om)
            
            current_meetings.append(meeting)
            min_rooms = max(min_rooms, len(current_meetings))
        
        return min_rooms

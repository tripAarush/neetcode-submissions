"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x:x.start)
        cur_end = 0
        for i in range(len(intervals)):
            if cur_end > intervals[i].start:
                return False
            cur_end = intervals[i].end

        return True 
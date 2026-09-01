"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        import heapq
        intervals.sort(key = lambda x: x.start)
        rooms = 0
        meetings = []
        for interval in intervals:
            if not meetings:
                rooms+=1
                heapq.heappush(meetings, interval.end)
                continue
            early = heapq.heappop(meetings)
            if early > interval.start:
                rooms+=1
                heapq.heappush(meetings, early)
            heapq.heappush(meetings, interval.end)

            
        return rooms
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        last = intervals[0]
        for i in range(1, len(intervals)):
            if last[1] <= intervals[i][0]:
                last = intervals[i]
            else:
                last[1] = min(last[1], intervals[i][1])
                res+=1
        return res
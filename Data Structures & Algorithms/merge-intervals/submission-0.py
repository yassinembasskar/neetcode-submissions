class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        new_intervals = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= new_intervals[-1][1]:
                new_intervals[-1][1] = max(intervals[i][1], new_intervals[-1][1])
            else:
                new_intervals.append(intervals[i])
        return new_intervals 
        
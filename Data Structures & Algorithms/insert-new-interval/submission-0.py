class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        new_intervals = []
        n = len(intervals)
        i = 0
        inserted = False
        while (i < n or not inserted):
            if (i < n and intervals[i][0] <= newInterval[0]) or inserted:
                if not new_intervals or intervals[i][0] > new_intervals[-1][1]:
                    new_intervals.append(intervals[i])
                else:
                    new_intervals[-1][1] = max(new_intervals[-1][1], intervals[i][1])
                i+=1
            else:
                if not new_intervals or newInterval[0] > new_intervals[-1][1]:
                    new_intervals.append(newInterval)
                else:
                    new_intervals[-1][1] = max(new_intervals[-1][1], newInterval[1])
                inserted = True
        return new_intervals
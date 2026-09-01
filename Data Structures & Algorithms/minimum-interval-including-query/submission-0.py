class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        import heapq
        result = []
        copy = queries.copy()
        copy.sort()
        intervals.sort()
        queue = []
        dictionnary = {}
        i = 0
        for q in copy:
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(queue, [intervals[i][1]-intervals[i][0]+1, intervals[i][1]])
                i+=1
            while queue:
                last = heapq.heappop(queue)
                if not last[1] < q:
                    dictionnary[q] = last[0]
                    heapq.heappush(queue, last)
                    break
        
        for q in queries:
            if q not in dictionnary:
                result.append(-1)
            else:
                result.append(dictionnary[q])
        return result
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dictionnary = {}
        for task in tasks:
            dictionnary[task] = dictionnary.get(task, 0) + 1
        import heapq
        from collections import deque
        waiting = deque()
        max_heap = []
        for key, item in dictionnary.items():
            heapq.heappush(max_heap, (-item, key))

        time = 0
        while max_heap or waiting:
            time+=1
            if max_heap:
                count, item = heapq.heappop(max_heap)
                count += 1
                if count < 0:
                    waiting.append((time+n, count, item))
            if waiting and waiting[0][0] == time:
                _, count, item = waiting.popleft()
                heapq.heappush(max_heap, (count, item))

        return time


        
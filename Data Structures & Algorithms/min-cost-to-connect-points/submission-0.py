class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return 0
        def distance(a, b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])
        import heapq
        dictionnary = {}
        minim = float("+inf")
        couple = None
        for i in range(len(points)):
            dictionnary[i] = []
            for j in range(len(points)):
                if i == j:
                    continue
                dist = distance(points[i], points[j])
                heapq.heappush(dictionnary[i], (dist,i,j))
                if dist < minim:
                    minim = dist
                    couple = (i, j)
        heapq.heappop(dictionnary[couple[0]])
        heapq.heappop(dictionnary[couple[1]])
        visited = set()
        visited.add(couple[0])
        visited.add(couple[1])
        visiting = set()
        queue = []
        while len(visited)!=len(points):
            for v in (visited - visiting):
                visiting.add(v)
                item = heapq.heappop(dictionnary[v])
                heapq.heappush(queue, item)
            item = heapq.heappop(queue)
            visiting.remove(item[1])
            if item[2] in visited:
                continue
            visited.add(item[2])
            minim+=item[0]
        return minim


        
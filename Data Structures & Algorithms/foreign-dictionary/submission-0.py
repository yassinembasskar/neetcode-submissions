class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        indegree = {}
        graph = {}
        import heapq
        for i in range(len(words)-1):
            itm1 = words[i]
            itm2 = words[i+1]
            if len(itm1) > len(itm2) and itm1[:len(itm2)] == itm2 :
                return ""
            for k in range(min(len(itm1), len(itm2))):
                if itm1[k] != itm2[k]:
                    if itm1[k] in graph and itm2[k] in graph[itm1[k]]:
                        break
                    if itm1[k] not in graph:
                        graph[itm1[k]] = set()
                    if itm2[k] not in indegree:
                        indegree[itm2[k]] = 0
                    graph[itm1[k]].add(itm2[k])
                    indegree[itm2[k]] += 1
                    break
        queue = []
        for word in words:
            for char in word:
                if char not in indegree:
                    indegree[char] = 0
                    heapq.heappush(queue, char)
        result = ""
        while queue:
            char = heapq.heappop(queue)
            if char in graph:
                for itm in graph[char]:
                    indegree[itm]-=1
                    if indegree[itm] == 0:
                        heapq.heappush(queue, itm)
            result = result + char
        if len(result) < len(indegree):
            return ""
        return result

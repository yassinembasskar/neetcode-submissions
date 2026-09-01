class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for pr in prerequisites:
            if pr[0] not in graph:
                graph[pr[0]] = set()
            graph[pr[0]].add(pr[1])
        
        visited = set()
        processed = set()
        def dfs(num):
            if num in visited:
                return False
            if num in processed:
                return True
            visited.add(num)
            if num in graph:
                for g in graph[num]:
                    if not dfs(g):
                        return False
            visited.remove(num)
            processed.add(num)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
            

        return True




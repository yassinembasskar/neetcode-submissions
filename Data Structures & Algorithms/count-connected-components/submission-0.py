class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dictionnary = {}
        for edge in edges:
            if edge[0] not in dictionnary:
                dictionnary[edge[0]] = set()
            if edge[1] not in dictionnary:
                dictionnary[edge[1]] = set()
            dictionnary[edge[0]].add(edge[1])
            dictionnary[edge[1]].add(edge[0])

        def backtrack(i, visited):
            if i in visited:
                return 0
            visited.add(i)
            if i not in dictionnary:
                return 1
            else:
                for j in dictionnary[i]:
                    backtrack(j, visited)
                return 1
        
        res = 0
        visited = set()
        for i in range(n):
            res += backtrack(i, visited)
        return res
            

            
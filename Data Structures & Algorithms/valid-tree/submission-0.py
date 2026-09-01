class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dictionnary = {}
        for pair in edges:
            if pair[0] not in dictionnary:
                dictionnary[pair[0]] = set()
            if pair[1] not in dictionnary:
                dictionnary[pair[1]] = set()
            dictionnary[pair[0]].add(pair[1])
            dictionnary[pair[1]].add(pair[0])
        
        def dfs(num, current, visited):
            if num in visited:
                return False
            visited.add(num)
            for son in dictionnary.get(num, set()):
                if son == current:
                    continue
                if not dfs(son, num, visited):
                    return False
            return True
            
        visited = set()
        if not dfs(0, -1, visited):
            return False
        return len(visited) == n
        
            
        
            
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memory = {}
        def dfs(i, j):
            if (i,j) in memory:
                return memory[(i,j)]
            if j == len(p):
                memory[(i,j)] = (i == len(s))
                return i == len(s)
            first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if j+1 < len(p) and p[j+1] == '*':
                if first_match:
                    memory[(i,j)] = dfs(i+1, j) or dfs(i, j+2)
                    return memory[(i,j)] 
                memory[(i,j)] = dfs(i, j+2)
                return memory[(i,j)] 
            memory[(i,j)] = first_match and dfs(i+1, j+1)
            return memory[(i,j)]
        return dfs(0,0)
            
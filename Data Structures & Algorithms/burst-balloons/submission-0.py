class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        new = [1] + nums[:] + [1]
        memory = {}
        def dfs(left, right):
            if (left, right) in memory:
                return memory[(left, right)]
            if right - left <= 1:
                return 0
            res = []
            for k in range(left+1, right):
                res.append(dfs(left, k)+ dfs(k, right) + new[left]*new[k]*new[right])
            memory[(left,right)] = max(res)
            return memory[(left, right)]
        return dfs(0, len(new)-1)
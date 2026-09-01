class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        length = len(cost)

        def helper(step):
            if step in memo:
                return memo[step]
            if step+2 >= length:
                memo[step] = cost[step]
                return cost[step]

            if step+1 in memo:
                res1 = memo[step+1] + cost[step]
            else:
                res1 = helper(step+1) + cost[step]

            if step + 2 in memo:
                res2 = memo[step+2] + cost[step]
            else:
                res2 = helper(step+2) + cost[step]
            
            res = min(res1, res2)
            memo[step] = res
            return res

        return min(helper(0), helper(1))

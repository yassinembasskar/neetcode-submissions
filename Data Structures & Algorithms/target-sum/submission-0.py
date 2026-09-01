class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = sum(nums)
        if target > n or target < -n:
            return 0
        dp = [0] * (2*n+1)
        dp[n] = 1
        for i in range(len(nums)):
            new_dp = [0] * (2*n + 1)
            for j in range(2*n+1):
                if j-nums[i] >= 0:
                    new_dp[j-nums[i]]+=dp[j]
                if j+nums[i] <= 2*n:
                    new_dp[j+nums[i]]+=dp[j]
            dp = new_dp
        return dp[target + n]
            
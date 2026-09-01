class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * len(coins) for _ in range(amount+1)]
        dp[amount][0] = 1
        for j in range(len(coins)):
            for i in range(amount, -1, -1):
                change = i - coins[j]
                if change >= 0:
                    dp[change][0] += dp[i][0]
        return dp[0][0]
                


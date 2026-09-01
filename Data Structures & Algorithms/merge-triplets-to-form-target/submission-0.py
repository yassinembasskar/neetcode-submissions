class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        dp = [[0,0,0,0] for _ in range(len(triplets))]
        for i in range(3):
            for j in range(len(triplets)):
                if triplets[j][i] == target[i]:
                    dp[j][i] = 1
                elif triplets[j][i] > target[i]:
                    dp[j][i] = 2
                    dp[j][3] = 1
        for i in range(3):
            has_one = False
            for item in dp:
                if item[3] == 1:
                    continue
                if item[i] == 1:
                    has_one = True
            if not has_one:
                return False

        return True
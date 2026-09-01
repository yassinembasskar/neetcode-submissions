class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dp(string):
            if string == "":
                return True
            elif string in memo:
                return memo[string]
            for word in wordDict:
                if string.startswith(word):
                    if dp(string[len(word):]):
                        memo[string[len(word):]] = True
                        return True
                    memo[string[len(word):]] = False
            return False
        return dp(s)
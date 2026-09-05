class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        i = 0
        n = len(word1)
        m = len(word2)
        while i < n and i < m:
            res += word1[i] + word2[i]
            i+=1
        while i < n:
            res += word1[i]
            i+=1
        while i < m:
            res += word2[i]
            i+=1
        return res
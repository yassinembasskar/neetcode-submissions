class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        max_length = 0
        length = 0
        for i in range(len(s)):
            if s[i] in chars:
                max_length = max(max_length, length)
                if chars[s[i]] >= i-length:
                    length = i - chars[s[i]]
                else:
                    length+=1
            else:
                length+=1
            chars[s[i]] = i


        return max(length, max_length)
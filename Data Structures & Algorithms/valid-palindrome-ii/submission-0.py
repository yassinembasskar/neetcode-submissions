class Solution:
    def validPalindrome(self, s: str) -> bool:
        breaking = (-1, -1)
        deleted = False
        right = len(s) - 1
        left = 0
        while left < right:
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                if breaking == (-1, -1):
                    breaking = (left, right)
                    right-=1
                else:
                    if deleted:
                        return False
                    left, right = breaking
                    deleted = True
                    left += 1
        return True
            
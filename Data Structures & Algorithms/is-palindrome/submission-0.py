class Solution:
    def isPalindrome(self, s: str) -> bool:
        characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
        s = [c for c in s.lower() if c in characters]
        right = len(s)-1
        left = 0
        while right > left:
            if s[right]!= s[left]:
                return False
            right-=1
            left+=1
            
        return True
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter
        left = 0
        right = 0
        max_cons = 0
        count = Counter()
        while right < len(s):
            if s[right] in count:
                count[s[right]]+=1
            else: 
                count[s[right]]=1
            if (right - left - count.most_common(1)[0][1] + 1) > k:
                count[s[left]]-=1
                left+=1
                
            right+=1

        return right - left
            


        
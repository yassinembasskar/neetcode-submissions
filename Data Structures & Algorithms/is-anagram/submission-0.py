class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        dictionnary_s = {}
        dictionnary_t = {}
        for l in letters:
            dictionnary_s[l] = 0
            dictionnary_t[l] = 0

        for c1 in s:
            dictionnary_s[c1]+=1
        for c2 in t: 
            dictionnary_t[c2]+=1
        
        for key, val in dictionnary_s.items():
            if dictionnary_t[key] != val:
                return False
        return True
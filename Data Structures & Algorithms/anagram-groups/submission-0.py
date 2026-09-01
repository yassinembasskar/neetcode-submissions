class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        dictionnaries = []
        letters = 'abcdefghijklmnopqrstuvwxyz'
        result = []
        for i in range(n):
            temp_dict = {}
            for l in strs[i]:
                if l not in temp_dict:
                    temp_dict[l] = 1
                else:
                    temp_dict[l]+=1
            dictionnaries.append(temp_dict)

        visited = set()
        for i in range(n-1):
            if i in visited:
                continue
            res = [strs[i]]
            visited.add(i)
            for j in range(i+1, n):
                if dictionnaries[i] == dictionnaries[j]:
                    res.append(strs[j])
                    visited.add(j)
            result.append(res)
        
        if n-1 not in visited:
            result.append([strs[n-1]])

        return result
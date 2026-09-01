class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        visited = {}
        sub_string = {}
        left = 0
        right = len(s1)-1

        for c1 in s1:
            visited[c1] = visited.get(c1, 0) + 1

        for i in range(right+1):
            sub_string[s2[i]] = sub_string.get(s2[i],0) + 1
        
        while right < len(s2)-1:
            if sub_string == visited:
                return True

            right+=1
            sub_string[s2[right]] = sub_string.get(s2[right], 0) + 1
            sub_string[s2[left]]-=1
            if sub_string[s2[left]] == 0:
                del sub_string[s2[left]] 
            left+=1

        return (sub_string == visited)
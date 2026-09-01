class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dictionnary = {}
        for i in range(len(s)):
            if s[i] in dictionnary:
                dictionnary[s[i]][1] = i
            else:
                dictionnary[s[i]] = [i, i]
        boundaries = []
        for key, val in dictionnary.items():
            if not boundaries or boundaries[-1][1] < val[0]:
                boundaries.append(val)
                continue
            if boundaries[-1][1] < val[1]:
                boundaries[-1][1] = val[1]
        result = []
        for bound in boundaries:
            result.append(bound[1] - bound[0] + 1)
        return result

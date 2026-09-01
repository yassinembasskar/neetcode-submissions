class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += '*|*' + s + "*|*"
        return res

    def decode(self, s: str) -> List[str]:
        result = s.split('*|*')
        if len(result) > 2:
            return result[1:-1:2]
        return []
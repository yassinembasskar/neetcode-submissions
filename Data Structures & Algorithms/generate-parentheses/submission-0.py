class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        res = set()
        combins = self.generateParenthesis(n-1)
        for comb in combins:
            for i in range(len(comb)):
                res.add(comb[:i] + "()" + comb[i:])
            res.add(comb + "()")
        return list(res)
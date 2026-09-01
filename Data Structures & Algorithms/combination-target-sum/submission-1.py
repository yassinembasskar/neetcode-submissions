class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target <= 1:
            return []
        candidates.sort()
        res = []
        for i in range(len(candidates)):
            if candidates[i] > target:
                break
            elif candidates[i] == target:
                res.extend([[candidates[i]]])
            else:
                combination = self.combinationSum(candidates[i:], target-candidates[i])
                res.extend([comb + [candidates[i]] for comb in combination if comb])
        return res

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if target <= 0:
            return None
        res = []
        candidates.sort()
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > target:
                break
            elif candidates[i] == target:
                res.append([candidates[i]])
                break
            else:
                new_combin = self.combinationSum2(candidates[i+1:], target - candidates[i])
                for comb in new_combin:
                    if comb is not None:
                        res.append([candidates[i]] + comb)
        return res
        
        
            
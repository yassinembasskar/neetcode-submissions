class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            remaining = nums[:i] + nums[i+1:]
            comb_remaining = self.permute(remaining)
            for rem in comb_remaining:
                res.append([nums[i]] + rem)
        return res

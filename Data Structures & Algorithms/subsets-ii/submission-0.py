class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], nums]
        
        nums.sort()
        res = [[]]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            nsubs = self.subsetsWithDup(nums[i+1:])
            res.extend([[nums[i]] + sub for sub in nsubs])
            
        return res
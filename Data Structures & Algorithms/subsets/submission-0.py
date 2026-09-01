class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], [nums[0]]]
        else:
            subset = self.subsets(nums[1:])
            newsub = [sub + [nums[0]] for sub in subset]
            subset.extend(newsub)
            return subset
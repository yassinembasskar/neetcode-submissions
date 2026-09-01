class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        items = set(nums)
        for i in range(len(nums)+1):
            if i not in items:
                return i
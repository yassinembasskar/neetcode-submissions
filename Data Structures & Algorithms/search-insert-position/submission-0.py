class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        n = len(nums)
        for num in nums:
            if num >= target:
                return i
            i+=1
        return n
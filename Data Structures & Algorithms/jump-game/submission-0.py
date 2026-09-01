class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        furtherest = 0
        for i in range(n):
            if i > furtherest:
                return False
            furtherest = max(furtherest, i+nums[i])
            if furtherest >= n:
                break
        return True
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = [0] * len(nums)
        dp_min = [0] * len(nums)
        dp_max[0] = dp_min[0] = result = nums[0]
        for i in range(1, len(nums)):
            dp_max[i] = max(nums[i]*dp_max[i-1], nums[i]*dp_min[i-1], nums[i])
            dp_min[i] = min(nums[i]*dp_max[i-1], nums[i]*dp_min[i-1], nums[i])
            result = max(result, dp_max[i])
        return result
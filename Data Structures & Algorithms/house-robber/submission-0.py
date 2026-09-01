class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memory = {}
        def dp(i):
            if i in memory:
                return memory[i]
            if i>=n:
                return 0
            elif i+1 == n:
                memory[i] = nums[i]
            elif i+2 == n:
                memory[i] = max(nums[i], nums[i+1])
            else:
                step1 = dp(i+2)
                step2 = dp(i+3)
                memory[i] = nums[i] + max(step1, step2)
            return memory[i]
        step1 = dp(0)
        step2 = dp(1)
        return max(step1, step2)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)
        memory = {0: {}, 1: {}}
        def dp(i, opt):
            # 0 is the range between 0 to n-1 and 1 is 1 to n
            if i in memory[opt]:
                return memory[opt][i]
            if opt == 0: last = n-1
            else: last = n

            if i>=last:
                return 0
            elif i+1 == last:
                memory[opt][i] = nums[i]
            elif i+2 == last:
                memory[opt][i] = max(nums[i], nums[i+1])
            else:
                step1 = dp(i+2, opt)
                step2 = dp(i+3, opt)
                memory[opt][i] = nums[i] + max(step1, step2)
            return memory[opt][i]
        step11 = dp(0, 0)
        step12 = dp(1, 0)
        step21 = dp(1, 1)
        step22 = dp(2, 1)
        return max(step11, step12, step21, step22)
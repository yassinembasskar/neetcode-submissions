class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if nums.count(0) > 1:
            return [0] * length
        mul = 1
        for n in nums:
            if n != 0:
                mul *= n
        if 0 in nums:
            res = [0] * length
            for i in range(length):
                if nums[i] == 0:
                    res[i] = mul
        
        else:
            res = [mul] * length
            for i in range(length):
                res[i] = int(res[i]/nums[i])

        return res

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        n = len(nums)
        somme = 0
        minim = float("+inf")
        while j <= n:
            if somme >= target:
                if j-i < minim:
                    minim = j-i
                somme -= nums[i]
                i+=1
            else:
                if j >= n:
                    break
                somme += nums[j]
                j+=1
        if minim == float("+inf"):
            return 0
        return minim
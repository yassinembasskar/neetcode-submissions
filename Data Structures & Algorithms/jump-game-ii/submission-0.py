class Solution:
    def jump(self, nums: List[int]) -> int:
        furtherest = 0
        min_jumps = 0
        boundary = 0
        n = len(nums)
        for i in range(n):
            if i > boundary:
                boundary = furtherest
                min_jumps+=1
                if boundary >= n-1:
                    break
            if furtherest < i + nums[i]:
                furtherest = i + nums[i]
        return min_jumps

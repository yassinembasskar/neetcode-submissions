class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = [-1] * 10000
        for n in nums:
            bits[n-1] += 1
        for n in set(nums):
            if bits[n-1] == 0:
                return n

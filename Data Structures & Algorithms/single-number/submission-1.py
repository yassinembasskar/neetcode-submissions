class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num]= 0
            counter[num] += 1
        for key, val in counter.items():
            if val == 1:
                return key
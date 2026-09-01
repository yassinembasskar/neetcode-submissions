class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remain = 1
        for i in range(len(digits)-1,-1,-1):
            val = digits[i]
            val += remain
            digits[i] = val % 10
            remain = val // 10
            if remain == 0:
                break
        if remain > 0:
            digits = [1] + digits
        return digits

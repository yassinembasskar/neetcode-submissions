class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 1:
            return 0
        elif x < 4:
            return 1
        else:
            left, right = 2, x // 2
            while left < right:
                mid = (left + right) // 2
                if mid == left or mid * mid == x:
                    return mid
                elif mid * mid < x:
                    left = mid
                elif mid * mid > x:
                    right = mid
            return left
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        minim = 1
        maxim = n
        while minim <= maxim:
            mid = (minim + maxim) // 2 
            guessing = guess(mid)
            if guessing == 1:
                minim = mid+1
            elif guessing == -1:
                maxim = mid-1
            else:
                return mid
        
        
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        if h == len(piles):
            return max(piles)
        
        high = max(piles)
        low = 0
        found = high
        while high > low:
            k = (high + low) // 2
            if k < 1:
                return 1
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            if hours > h:
                low = k + 1
            elif hours <= h:
                high = k
                

        if low == high:
            return low


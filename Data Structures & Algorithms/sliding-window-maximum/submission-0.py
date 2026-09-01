class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        if k == 1:
            return nums
        res = []
        d = deque([0])

        for i in range(1,len(nums)):
            while d and nums[i] > nums[d[-1]]:
                d.pop()
            d.append(i)
            
            if i >= k-1:
                if d[0] <= i-k:
                    d.popleft()
                res.append(nums[d[0]])
        
        return res
                

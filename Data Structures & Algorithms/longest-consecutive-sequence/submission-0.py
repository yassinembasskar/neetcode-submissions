class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set()
        numbers_set = set(nums)
        max_streak = 0
        for n in nums:
            if n-1 in numbers_set or n in visited:
                continue
            streak = 1
            next_number = n+1
            while(next_number in numbers_set):
                next_number+=1
                streak+=1
            if streak > max_streak:
                max_streak = streak
                
            visited.add(n)

        return max_streak
        
        

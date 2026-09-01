class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = set()
        for i in range(len(nums)):
            if nums[i] in visited:
                return nums[i]
            visited.add(nums[i])
            

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        results = []
        visited = {}
        last = float("-inf")
        for i in range(len(nums)-2):
            if last == nums[i]:
                continue
            last = nums[i]
            right = len(nums)-1
            left = i+1
            while right > left:
                val = nums[right] + nums[left]
                if (val + last == 0 and (nums[i], nums[left], nums[right]) not in visited):
                    results.append([nums[i], nums[left], nums[right]])
                    visited[(nums[i], nums[left], nums[right])] = True
                elif (val + last < 0):
                    left+=1
                else:
                    right-=1
        return results
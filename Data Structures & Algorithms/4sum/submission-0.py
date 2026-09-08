class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        if n < 4:
            return []
        res = []
        seen = set()
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j]==nums[j-1]:
                    continue
                start = j+1 
                end = n-1
                while start < end:
                    if nums[start] + nums[end] > target - nums[i] - nums[j]:
                        end-=1
                    elif nums[start] + nums[end] < target - nums[i] - nums[j]:
                        start+=1
                    else:
                        if (nums[i], nums[j], nums[start], nums[end]) not in seen:
                            seen.add((nums[i], nums[j], nums[start], nums[end]))
                            res.append([nums[i], nums[j], nums[start], nums[end]])
                            start+=1
                            end-=1
                            while start<end and nums[start]==nums[start-1]:
                                start += 1
                            while end>start and nums[end]==nums[end+1]:
                                end -= 1
        return res

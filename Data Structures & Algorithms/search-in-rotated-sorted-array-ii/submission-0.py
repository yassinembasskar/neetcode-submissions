class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                return True
            if nums[mid] < nums[start]:
                if nums[mid] < target <= nums[end]:
                    start = mid+1
                else:
                    end = mid-1
            elif nums[mid] > nums[end]:
                if nums[start] <= target < nums[mid]: 
                    end = mid-1
                else:
                    start = mid+1
            else:
                if nums[start] == nums[end]:
                    start += 1
                elif nums[mid] > target:
                    end = mid-1
                else:
                    start = mid+1
        return False
                


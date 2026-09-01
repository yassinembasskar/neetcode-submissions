class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[left] < nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                elif target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    return mid
            elif nums[left] >= nums[mid]:
                if left == mid:
                    if nums[left] == target:
                        return left
                    else:
                        left = mid + 1
                elif target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                elif target > nums[right] or target < nums[mid]:
                    right = mid - 1
                else:
                    return mid
        return -1

        
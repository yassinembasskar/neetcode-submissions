class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for i in range(len(nums)):
            if nums[i] in indexes:
                indexes[nums[i]].append(i)
            else:
                indexes[nums[i]] = [i]

        for key, val in indexes.items():
            diff = (target - key)
            if diff in indexes and val[0] != indexes[diff][-1]:
                return [val[0], indexes[diff][-1]]
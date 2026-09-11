class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        windows = set()
        for i in range(len(nums)):
            if nums[i] in windows:
                return True
            windows.add(nums[i])
            if len(windows) > k:
                windows.remove(nums[i-k])
        return False
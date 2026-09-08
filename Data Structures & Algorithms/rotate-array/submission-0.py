class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        def reverse_list(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start+=1
                end-=1
        reverse_list(0, len(nums)-1)
        reverse_list(0, k-1)
        reverse_list(k, len(nums)-1)
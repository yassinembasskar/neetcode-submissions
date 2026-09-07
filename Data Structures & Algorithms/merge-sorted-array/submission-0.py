class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = m - 1
        i = n - 1
        c = m + n - 1
        while j >= 0 and i >= 0:
            if nums1[j] > nums2[i]:
                nums1[c] = nums1[j]
                j-=1
            else:
                nums1[c] = nums2[i]
                i-=1
            c-=1
        while i >= 0:
            nums1[c] = nums2[i]
            i-=1
            c-=1
        
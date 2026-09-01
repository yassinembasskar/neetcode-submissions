class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        if n==0:
            return (nums1[m//2] + nums1[(m-1)//2])/2
        if m==0:
            return (nums2[n//2] + nums2[(n-1)//2])/2

        low = 0
        high = m
        half = (m + n + 1) // 2

        while(low <= high):
            i = (low + high) // 2
            j = half - i
            if i > 0:
                left1 = nums1[i-1]
            else:
                left1 = float("-inf")
            
            if j > 0:
                left2 = nums2[j-1]
            else:
                left2 = float("-inf")
            
            if i < m:
                right1 = nums1[i]
            else:
                right1 = float("+inf")
            
            if j < n:
                right2 = nums2[j]
            else:
                right2 = float("+inf")
        
            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2) 
            
            elif left1 > right2:
                high = i - 1
            elif left2 > right1:
                low = i + 1
        
            

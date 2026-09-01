class Solution:
    def maxArea(self, height: List[int]) -> int:
        right = len(height) - 1
        left = 0
        maximum = 0
        while(right > left):
            minimum = min(height[left],height[right])
            if minimum * (right - left) > maximum:
                maximum = minimum * (right - left)
            if height[right]> height[left]:
                left+=1
            else:
                right-=1
        return maximum

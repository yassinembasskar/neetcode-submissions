class Solution:
    def trap(self, height: List[int]) -> int:
        right = len(height) - 1
        left = 0
        depth = 0
        max_depth = 0
        while(right > left):
            val = min(height[left], height[right])
            if height[right] > height[left]:
                depth += max(max_depth - height[left], 0)
                left+=1
            elif height[right] < height[left]:
                depth += max(max_depth - height[right], 0)
                right-=1
            else:
                depth+= max(max_depth - height[right], 0)
                depth+= max(max_depth - height[left], 0)
                left+=1
                right-=1
            if val > max_depth:
                max_depth = val

        if left == right:
            depth += max(max_depth - height[left], 0)
            
        return depth
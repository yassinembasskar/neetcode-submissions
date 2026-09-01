class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest = 0
        for i in range(len(heights)):
            if not stack or stack[-1][0] < heights[i]:
                stack.append([heights[i], i])
                continue
            
            last = False
            while stack and stack[-1][0] > heights[i]:
                if largest < stack[-1][0] * (i - stack[-1][1]):
                    largest = stack[-1][0] * (i - stack[-1][1])
                last = stack.pop()
            if last:
                stack.append([heights[i], last[1]])
            

        while stack:
            if largest < stack[-1][0] * (len(heights) - stack[-1][1]):
                largest = stack[-1][0] * (len(heights) - stack[-1][1])
            stack.pop()
            
        return largest

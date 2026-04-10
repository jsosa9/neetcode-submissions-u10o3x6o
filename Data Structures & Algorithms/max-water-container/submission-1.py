class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currentMax = 0
        for i, h in enumerate(heights):
            right = len(heights) - 1
            left = i 
            while left < right:
                width = right - left
                if heights[left] < heights[right]:
                    height = heights[left]
                else:
                    height = heights[right]
                curr = int(height) * int(width)
                if curr > currentMax:
                    currentMax = curr
                right-=1
        return currentMax
        
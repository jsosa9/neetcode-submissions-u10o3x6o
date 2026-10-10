class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1
        width = 0
        height = 10000000
        total = 0
        while l < r:
            width = r - l 
            height = min(heights[l], heights[r])
            total = max(width * height, total)
            if heights[l] < heights[r]:
                l += 1
            else:
                r-=1
        return total

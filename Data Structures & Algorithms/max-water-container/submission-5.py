class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1
        re = 0

        while l < r:
            width = r - l 
            area = width * min(heights[l], heights[r])
            re = max(re, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return re
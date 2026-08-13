class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        so you find 2 bars and then right - left * smallest bar is the amount of water 
        """

        l, r = 0, len(heights) - 1
        top = 0
        while l < r: 
            top = max(min(heights[l], heights[r]) * (r - l), top)
            if heights[l] > heights[r]:
                r-=1 
            else:
                l+=1
        return top 
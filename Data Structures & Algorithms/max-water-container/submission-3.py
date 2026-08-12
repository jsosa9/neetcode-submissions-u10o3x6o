class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        so you must find 2 bars 
        pick the lowest bar and then mulitply it by the space between 

        pick the first and last nodes 
        """
        l, r = 0, len(heights) - 1
        top = 0
        while l < r:
            top = max(top, min(heights[l],heights[r]) * (r-l))
            if heights[l] < heights[r]:
                l+=1 
            else:
                r-=1 
        return top
            
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        so basically i need to find the max height
        """
        left, right = 0, len(heights) - 1 
        max_area = 0
        while left < right: 
            area = min(heights[left], heights[right]) * (right - left)
            max_area = max(max_area, area)
            if heights[left] < heights[right]:
                left+=1
            elif heights[left] > heights[right]:
                right-=1
            else:
                left+=1
        return max_area

        
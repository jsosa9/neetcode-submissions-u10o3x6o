class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        re = 0
        while l < r: 
            w = r - l
            lo = min(heights[l], heights[r])
            c = w * lo

            if heights[l] == heights[r]:
                r -= 1
                re = max(re,c)
            elif heights[l] < heights[r]:
                l+= 1
                re = max(re,c)
            else:
                r-=1
                re = max(re,c)
        return re
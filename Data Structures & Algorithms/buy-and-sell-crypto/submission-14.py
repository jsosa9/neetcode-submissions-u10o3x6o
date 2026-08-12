class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        2 pointers we only care about the 2 values and not whats in the middle 
        """
        l, r = 0, 1
        top = 0
        while r < len(prices):
            top = max(top, prices[r] - prices[l])
            if prices[r] < prices[l]:
                #inc left because left is too big 
                l+=1
            else:
                # dec right because right is too small 
                r+=1
        return top
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        """
        l, r = 0, 1
        top = 0 

        while r < len(prices):
            top = max(top, prices[r] - prices[l])

            if prices[r] < prices[l]:
                l+=1
            else:
                r+=1
        return top 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        top = 0
        while r < len(prices):
            if prices[r] - prices[l] < 0:
                l=r
            else:
                if prices[r] - prices[l] > top:
                    top = prices[r] - prices[l]
            r+=1
        return top

            
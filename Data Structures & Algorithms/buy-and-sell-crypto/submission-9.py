class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ 

        so we want to buy at a low price and sell high
        buy at 1 and sell after taht at the hgihest number

         so we iterate through it until we see the value one (shifitng the left pointer)
         keep the right pointer at the end 
         if left < right when we continue 
        """   
        l, r = 0, 1
        buy = prices[0]
        profit = 0 
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                buy = min(buy, prices[l])
                r+=1
            else:
                profit = max(profit, prices[r] - buy)
                r+=1
        return profit


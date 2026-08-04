class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        so you go through the array you find the lowest number from left to right 
        and then you find the lowerst on the left keep that there and then find the highest that comes after it and then do pointer 2 - pointer 1 
        """
        left, right = 0, 1 
        max_l = 0
        max_r = 0
        max_p = 0
        # we incremeent left when right - left is negative 
        # decfrease right when right - left is positive (we want max)
        while right - len(prices): 
            y = prices[right] - prices[left]
            print(prices[right])
            print(prices[left])
            print(y)
            print('      ')
            if y < 0:
                left = right 
            else:
                if y > max_p:
                    # print(max_p)
                    max_p = y 
                    max_l = left
                    max_r = right
            right += 1
        return max_p

                

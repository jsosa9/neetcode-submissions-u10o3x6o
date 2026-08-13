class Solution:
    def climbStairs(self, n: int) -> int:
        """
        1  1 
        2  2 
        3  1 + 2 
        4  2 + 2 or 1 + 1 + 1 + 1 or 2 + 1 + 1 
        5 2 + 2 + 1 or 2 + 1 + 1 + 1 or + 1 + 1 + 1 + 1 + 1 or 
        """
        memo = {1 : 1, 2 : 2}
        def f(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = f(n-2) + f(n-1)
                return memo[n]
        return f(n)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        so we're just doing the same thing as longest island but this time 
        we will instead count the size of the largest isalnd 
        """ 
        print('x')
        m,n = len(grid),len(grid[0])
        print('y')
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return 0
            else:
                grid[i][j] = 0
                return 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)
        x = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x = max(x, dfs(i,j))
        return x 



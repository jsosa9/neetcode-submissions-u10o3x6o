class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        0 - water 1 - land 

        * so we want to iterate throuhg each element of the grid 
        * if we encounter a piece of land we run dfs on it and then increment that count for each dfs iteration 
        * we have a max count whihc keeps track of hte higest one we found 
        """
        f_count = 0
        def dfs(i,j):
            count = 1
            grid[i][j] = 0 
            # down
            if i + 1 < len(grid) and grid[i + 1][j] == 1:
                count += dfs(i + 1, j)
            # up
            if i - 1 >= 0 and grid[i - 1][j] == 1:
                count += dfs(i - 1, j)
            # right
            if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                count += dfs(i, j + 1)
            # left 
            if j - 1 >= 0 and grid[i][j - 1] == 1:
                count += dfs(i, j - 1)
            return count 
            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    f_count = max(f_count, area)
        return f_count

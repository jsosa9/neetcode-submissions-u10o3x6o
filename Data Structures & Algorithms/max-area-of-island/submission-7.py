class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        so instead of increment the island for the first 1 we inc each instance of it 
        """
        top = 0 
        def dfs(i, j):
            grid[i][j] = 0
            count = 1
            if i > 0 and grid[i - 1][j] == 1:
                count += dfs(i - 1, j)
            if j > 0 and grid[i][j - 1] == 1:
                count += dfs(i, j - 1)
            if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                count += dfs(i, j + 1)
            if i < len(grid) - 1 and grid[i + 1][j] == 1:
                count += dfs(i + 1, j)
            return count
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x = dfs(i,j)
                    print(x)
                    top = max(top, x)
        return top 
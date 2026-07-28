class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #row and col
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i >= m or i < 0 or j >= n or j < 0 or grid[i][j] != '1':
                return 
            else:
                grid[i][j] = '0'
                dfs(i+1, j)
                dfs(i, j+1)
                dfs(i-1, j)
                dfs(i, j-1)
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1 
                    dfs(i,j)
        return islands
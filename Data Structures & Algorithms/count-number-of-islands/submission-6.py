class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        so everytime we discover a new 1 we increase the isalnd count and then continue checking the adj points 
        """
        total = 0
        def dfs(i,j):
            grid[i][j] = 0
            if i > 0 and grid[i - 1][j] == '1':
                dfs(i-1,j)
            if j > 0 and grid[i][j - 1] == '1':
                dfs(i,j-1)
            if i < len(grid) - 1 and grid[i + 1][j] == '1':
                dfs(i + 1, j)
            if j < len(grid[0]) - 1 and grid[i][j + 1] == '1':
                dfs(i, j + 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    total +=1 
        return total
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        same as number of islands but this time your counting the 
        the highest amount of consecutive 1's 
        """
        # row and col
        m, n = len(grid), len(grid[0])
        # longest count that we check 
        def dfs(i,j):
            # so with this dfs we would have to begin counting the longest streak
            # checking if this is a valid idx 
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return 0 
            else:
                # so this is where we burn the island but also we would have to return the recurison count 
                grid[i][j] = 0
                return 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # changing max area 
                    max_area = max(max_area, dfs(i, j))
        return max_area 

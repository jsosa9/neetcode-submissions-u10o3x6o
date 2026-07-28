class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # m = rows n = col
        m, n = len(grid), len(grid[0])
        def dfs(i,j):
            # i < 0 whihc means row is to high 
            # i >= m this means your oout of bounds in bounds is 0 to m - 1
            # j < 0 then your too far to the left 
            # j >= n means your out of bounds on the right
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return 
            # if its not valid then we set the current island to 0 and then check the neighboring ones with dfs 
            else:
                grid[i][j] = '0'
                dfs(i, j+1)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i-1, j)
        num_islands = 0
        # for all the values in range of the length of the grid, and all of the values in range for the row 
        for i in range(m):
            for j in range(n):
                # if the grid item is 1 meaning its valid we incrememnt the island and tehn call dfs to avoid double counting
                if grid[i][j] =='1':
                    num_islands += 1
                    dfs(i, j)
                    
        return num_islands
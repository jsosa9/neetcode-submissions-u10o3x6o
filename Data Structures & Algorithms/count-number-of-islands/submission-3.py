class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        The point of the problem is to find the number of island 
        an island is represented by a 1, water is represented by a 0

        for every island that we find we need to find the connected islands 
        if its not a island then we just continue 

        can go with a dfs or bfs i'll do dfs since im more comfortable 
        """
        # rows and columns 
        m, n = len(grid), len(grid[0])
        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return 
            else:
                # marked with a 0 to show that its been visited
                grid[i][j] = '0'
                dfs(i+1, j)
                dfs(i, j+1)
                dfs(i-1, j)
                dfs(i, j-1)

        island = 0
        # so for each row and for each column, if the value is 1 menaing island we call dfs and incremeent islad 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    island += 1 
                    dfs(i,j)
        return island  
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        so if im not mistaken once we find a 1 which is a piece of land we 
        incremenet the count and then we continue searching throuhg the adjacent islands 

        if we find 1's via the adj islands they dont count but if we find it outside of 
        the adj isalnds then the

        from what i know the dfs is used for recruison we're not using it in general like 
        we have a general search first and hten we call the dfs for recruisoin aspect to
        it 
        """
        total = 0 
        # i = cols  
        # j = rows
        # grid is just the current grid since we're updating things 
        def dfs(grid, i, j):
            """
            the goal of the dfs is to mark the current one as seen 
            and then check the ones above, below, right, and left of it 
            """
            grid[i][j] = '0'
            if i + 1 <= len(grid) - 1 and grid[i+1][j] == '1':
                dfs(grid, i+1, j)
            if i != 0 and grid[i-1][j] == '1':
                dfs(grid, i-1, j)
            if j + 1 <= len(grid[0]) - 1 and grid[i][j+1] == '1':
                dfs(grid, i, j+1)
            if j != 0 and grid[i][j - 1] == '1':
                dfs(grid, i, j-1)

        # getting the row and col only issue is that this only gets the first row 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # so i suppose im struggling to properly traverse through the grid 
                # but we have to go throgh each one mark it as 0 to mark it and then run dfs 
                if grid[i][j] == '1':
                    # didnt personally think to pass in the grid as a param but when peeking at the solution to see if i iterated properly throuhg the grid whcih i was i saw grid as a param in the dfs but other then that everything good so far 
                    dfs(grid, i, j)
                    total += 1
        return total 
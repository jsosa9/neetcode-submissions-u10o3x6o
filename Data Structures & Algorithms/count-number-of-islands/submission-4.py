class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        each piece of land is a 1 and each 0 is water 

        so we want to look for all the 1's using dfs and once we go deep enough and find a 1 
        we then have to look at the neighboring pieces 

        so dfs handles the recurison we have to handle finding the 1's 
        """
        def dfs(grid, r, c):
            # this needs to handle finding all the connected 1's 

            # if the current one is a 1 we turn it into 0 so its read 
            if grid[r][c] == '1':
                grid[r][c] = '0'
            # check if the right top left bottom is in bounds if so we check it and then recrusively call dfs on it 
            # if r != 0:
            if r - 1 >= 0 and grid[r-1][c] == '1':
                dfs(grid, r-1, c)
            if r + 1 < len(grid) and grid[r+1][c] == '1':
                dfs(grid, r+1, c)
            if c + 1 < len(grid[0]) and grid[r][c+1] == '1':
                dfs(grid, r, c+1)
            if c - 1 >= 0 and grid[r][c-1] == '1':
                dfs(grid, r, c-1)

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    count+=1
                    dfs(grid, r, c)
        return count
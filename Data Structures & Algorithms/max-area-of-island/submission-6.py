class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        so i need to find the amount of 1's the most amoutn of consectuive 1's linked together 

        this time the numbers are strings which is nice 

        so i need to iterate throuhg it and once i find a 1 the streak starts and i use dfs to look around it until its all 0 and then i have a var called count and then i take the max for it everytime to make sure that the var stored is onyl the max 
        """
        count = 0 
        t_count = 0

        def dfs(i, j, count):
            grid[i][j] = 0
            count = 1
            if i != 0 and grid[i - 1][j] == 1:
                count += dfs(i - 1, j, count)
            if j != 0 and grid[i][j - 1] == 1:
                count += dfs(i, j - 1, count)
            if i < len(grid) - 1 and grid[i + 1][j] == 1:
                count += dfs(i + 1, j, count)
            if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                count += dfs(i, j + 1, count)
            return count
            


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # i = row , j = col
                if grid[i][j] == 1:
                    # t_count = (t_count, count)
                    count = 0 
                    count += 1 
                    x = dfs(i, j, count)
                    print(x)
                    if x > t_count:
                        t_count = x
                
        return t_count 
                    

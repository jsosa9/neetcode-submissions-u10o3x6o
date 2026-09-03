class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        0 is treasure 
        -1 is water we cannot go on it 
        inf = 2147483647

        each land (2147483647) gets filled with the distnace it is from a treasure chest (0)

        if land cannot fill with treasure chest then value stays as 2147483647
        """
        v = 2147483647

        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append([i,j])

        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                # up down 
                if i > 0 and grid[i - 1][j] == v:
                    grid[i - 1][j] = grid[i][j] + 1 
                    queue.append([i - 1,j])
                if i < len(grid) - 1 and grid[i + 1][j] == v:
                    grid[i + 1][j] = grid[i][j] + 1 
                    queue.append([i + 1,j])
                
                # left right
                if j > 0 and grid[i][j - 1] == v:
                    grid[i][j - 1] = grid[i][j] + 1 
                    queue.append([i,j - 1])
                if j < len(grid[0]) - 1 and grid[i][j + 1] == v:
                    grid[i][j + 1] = grid[i][j] + 1 
                    queue.append([i,j + 1])
                

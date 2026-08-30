class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        so for every fresh fruit adajcent to the rotten fruit, that fresh fruit becoems rotten

        every step is a minute 

        and i have to retunr the min amount of minutes for 0 fresh fruit 
        """
        fresh = 0 
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i,j])
                if grid[i][j] == 1:
                    fresh += 1
        minutes = 0 
        while queue and fresh > 0:
            for _ in range(len(queue)):
                i,j = queue.popleft()
                # up
                if i > 0 and grid[i - 1][j] == 1:
                    grid[i-1][j] = 2
                    queue.append([i-1,j])
                    fresh-=1
                #down 
                if j > 0 and grid[i][j - 1] == 1:
                    grid[i][j-1] = 2
                    queue.append([i, j-1])
                    fresh-=1
                #left
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    grid[i+1][j] = 2
                    queue.append([i+1,j])
                    fresh-=1
                #right 
                if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                    grid[i][j+1] = 2
                    queue.append([i,j+1])
                    fresh-=1
            minutes += 1
        if fresh == 0:
            return minutes
        return -1

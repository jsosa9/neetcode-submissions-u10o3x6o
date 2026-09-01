class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        so what i recall from bfs is that you basically have to use the queue in order to add things to it 
        and then with the queuue that tells you the elements you have to look at and then you sort throuhg those elements 

        and this one we want the shortest count of 
        """
        fresh = 0 
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1 
                if grid[i][j] == 2:
                    queue.append([i,j])

        minutes = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                # mark the current one as seen
                # now we need to check all directions for fresh fruit and make them into rotten fruit and append to the queue
                i, j = queue.popleft() 
                if i > 0 and grid[i - 1][j] == 1:
                    grid[i-1][j] = 2 
                    queue.append([i-1, j])
                    fresh-=1
                if j > 0 and grid[i][j - 1] == 1:
                    grid[i][j - 1] = 2 
                    queue.append([i, j - 1])
                    fresh-=1
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    grid[i + 1][j] = 2 
                    queue.append([i+1, j])
                    fresh-=1
                if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2 
                    queue.append([i, j + 1])
                    fresh-=1
            minutes += 1
        if fresh == 0:
            return minutes
        else:
            return -1 
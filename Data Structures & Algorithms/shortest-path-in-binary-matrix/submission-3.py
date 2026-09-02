class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if grid[0][0] != 0 or grid[rows-1][cols-1] != 0:
            return -1 
        
        """

        """
        
        directions = [
            [-1,0],
            [-1,-1],
            [-1,1],
            [0,1],
            [0,-1],
            [1,0],
            [1,1],
            [1,-1]
        ]
        queue = deque()
        queue.append([0,0])
        grid[0][0] = 1 
        s = 1
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if rows - 1 == i and j == cols - 1:
                    return s 
                for a, b in directions:
                    na = a + i  
                    nb = b + j
                    if 0 <= na < cols and 0 <= nb < rows and grid[na][nb] == 0: 
                        grid[na][nb] = 1
                        queue.append([na,nb])
            s+=1
        return -1
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        """
        row = len(grid)
        col = len(grid[0])

        if grid[0][0] != 0 or grid[row - 1][col - 1] != 0: 
            return -1 

        
        directions = [
            [-1,-1],
            [-1,0],
            [-1,1],
            [0,1],
            [0,-1],
            [1,0],
            [1,-1],
            [1,1],
        ]
        queue = deque()
        queue.append([0,0])
        grid[0][0] = 1

        count = 1
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if i == row - 1 and j == col - 1:
                    return count 
                for a,b in directions:
                    na = a + i
                    nb = b + j


                    if 0 <= na < col and 0 <= nb < row and grid[na][nb] == 0:
                        grid[na][nb] = 1
                        queue.append([na,nb])
            count += 1 
        return -1 
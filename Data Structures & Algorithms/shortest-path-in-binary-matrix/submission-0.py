class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        so we only care about the shortst path from top left to bottom right 
        """
        # len of row 
        col = len(grid[0])
        # len of col 
        rows = len(grid)

        # checking if top left and bottom right are 0 to begin with if so continue else we stop 
        if grid[0][0] != 0 or grid[rows - 1][col - 1] != 0:
            return -1
        
        directions = [
            [1,-1],
            [1,1],
            [1,0],
            [0,1],
            [0,-1],
            [-1,0],
            [-1,1],
            [-1,-1]
        ]

        queue = deque()
        queue.append([0,0])
        grid[0][0] = 1
        p = 1
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if i == rows - 1 and j == col - 1:
                    return p
                for a, b in directions:
                    na = a + i
                    nb = b + j

                    if 0 <= na < rows and 0 <= nb < col and grid[na][nb] == 0:
                                grid[na][nb] = 1
                                queue.append([na,nb])
            p+=1 
                

        
        return -1
            # dfs logic but because we need diagonal we have to make some sort of directions arr 


        
        


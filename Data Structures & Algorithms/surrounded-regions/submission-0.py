class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        the logic for this one is if its on the edge then its safe becuase 
        it has one block that isn't surrounded by x
        """

        def dfs(i, j):
            board[i][j] = "S"
            if i > 0 and board[i - 1][j] == "O":
                dfs(i - 1,j)
            if j > 0 and board[i][j - 1] == "O":
                dfs(i,j - 1)
            if i < len(board) - 1 and board[i + 1][j] == "O":
                dfs(i + 1, j)
            if j < len(board[0]) - 1 and board[i][j + 1] == "O":
                dfs(i, j + 1)



        for i in range(len(board)):
            for j in range(len(board[0])):
                # so if its on the edge and its 0 then we continue to run dfs from there and mark them safe 
                if board[i][j] == "O":
                    if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
                        dfs(i,j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                # turn the O into X and turn the S into O 
                if board[i][j] == "O":
                    board[i][j] = "X"
        for i in range(len(board)):
            for j in range(len(board[0])):
                # turn the O into X and turn the S into O 
                if board[i][j] == "S":
                    board[i][j] = "O"
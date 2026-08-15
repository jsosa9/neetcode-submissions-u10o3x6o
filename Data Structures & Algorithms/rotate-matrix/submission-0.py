class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        1 : for every row, for each pair of [r][c] swap it so its [c][r]
        2 : 

        [1,2]
        [3,4]

        1 transpose
        1 = [0][0] -> [0][0]
        2 = [0][1] -> [1][0]
        3 = [1][0] -> [0][1]
        4 = [1][1] -> [1][1]
        [1, 3]
        [2, 4]

        2 reverse 
        [3, 1]
        [4, 2]
        """

        for c in range(len(matrix)):
            for j in range(c + 1, len(matrix)):
                matrix[c][j], matrix[j][c] = matrix[j][c], matrix[c][j]
        
        for row in matrix:
            row.reverse()
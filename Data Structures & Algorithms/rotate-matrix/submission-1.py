class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        so in order to shift 90 deg you have to swap every index at i,j with j,i 
        and then for every row we have to reverse it 
        """
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
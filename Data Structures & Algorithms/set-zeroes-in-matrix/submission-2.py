class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        so for each eleemnt in the matrix we have to check if its 0
        if its 0 we need to take that entire row and set it to 0 

        what if i used what was used to traverse matrix for this so for each elemnt 
        """ 
        r = set()
        col = set()
        for c in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[c][j] == 0:
                    r.add(c)
                    col.add(j)
                # if matrix[j][c] == 0:
                #     r.add(j)
                #     col.add(c)

        for l in r:
            for n in range(len(matrix[0])):
                matrix[l][n] = 0
        
        for l in col:
            for n in range(len(matrix)):
                matrix[n][l] = 0


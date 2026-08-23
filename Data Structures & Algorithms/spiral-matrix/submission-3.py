class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        this is when you have to move it from 
        top left to top right 
        2nd to top right to bottom right 
        2nd to bottome right to bottom left 
        then one up from bottom left to top - 1 
        """

        left, right = 0, len(matrix[0]) - 1 
        top, bottom = 0, len(matrix) - 1
        
        res = []
        while top <= bottom and left <= right:
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1 

            for c in range(top, bottom + 1):
                res.append(matrix[c][right])
            right -= 1 

            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
            bottom -= 1 

            if left <= right:
                for c in range(bottom, top - 1, -1):
                    res.append(matrix[c][left])
            left += 1 

        return res
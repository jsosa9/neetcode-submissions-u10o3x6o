class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """ 
        1 : go left to right 
        2 : go down the right side 
        3 : go from bottom right to bottom left 
        4 : go from bottom left to top left 
        """
        top, bottom = 0, len(matrix) - 1 
        left, right = 0, len(matrix[0]) - 1
        result = []
        while left <= right and top <= bottom: 
            # 1  
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1

            # 2 
            for c in range(top, bottom + 1):
                result.append(matrix[c][right])
            right -= 1 

            # 3 
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
            bottom -= 1
            # 4 
            if left <= right:
                for c in range(bottom, top - 1, -1):
                    result.append(matrix[c][left])
            left += 1
        return result 
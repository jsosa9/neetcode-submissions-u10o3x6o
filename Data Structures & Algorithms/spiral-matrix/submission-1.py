class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        """

        # height and width 
        top, bottom = 0, len(matrix) - 1 
        left, right = 0, len(matrix[0]) - 1

        # output 
        result = []
        while left <= right and top <= bottom:
            # from top left to top right 
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1
            # from top right to bottom right 
            for c in range(top, bottom + 1):
                result.append(matrix[c][right])
            right -= 1 
            # from bottom right to bottom left 
            if top <= bottom: 
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1 
            # from bottom left to top mid 
            if left <= right: 
                for c in range(bottom, top - 1, -1):
                    result.append(matrix[c][left])
                left += 1 
        return result
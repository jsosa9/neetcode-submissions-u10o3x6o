class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """

        """
        # now we need to look through the first one and then take note of the value we're changing and then call dfs based on it 
        def dfs(i,j):
            image[i][j] = color
            if i > 0 and image[i - 1][j] == val:
                dfs(i-1,j)
            if j > 0 and image[i][j - 1] == val:
                dfs(i,j-1)
            if i < len(image) - 1 and image[i + 1][j] == val:
                dfs(i + 1, j)
            if j < len(image[0]) - 1 and image[i][j + 1] == val:
                dfs(i, j + 1)

        val = 0 
        if image[sr][sc] == color:
            return image
        else:
            val = image[sr][sc]
            dfs(sr, sc)
        return image
        
        
            
            

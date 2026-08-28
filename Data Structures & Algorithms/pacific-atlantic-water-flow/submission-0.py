class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        atlantic = bottom and right side 
        pacific = top and left 
        """
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(i, j, visited):
            visited.add((i, j))

            # up
            if i > 0 and (i - 1, j) not in visited and heights[i - 1][j] >= heights[i][j]:
                dfs(i - 1, j, visited)

            # left
            if j > 0 and (i, j - 1) not in visited and heights[i][j - 1] >= heights[i][j]:
                dfs(i, j - 1, visited)

            # down
            if i < rows - 1 and (i + 1, j) not in visited and heights[i + 1][j] >= heights[i][j]:
                dfs(i + 1, j, visited)

            # right
            if j < cols - 1 and (i, j + 1) not in visited and heights[i][j + 1] >= heights[i][j]:
                dfs(i, j + 1, visited)

        # top row = Pacific
        # bottom row = Atlantic
        for j in range(cols):
            dfs(0, j, pacific)
            dfs(rows - 1, j, atlantic)

        # left column = Pacific
        # right column = Atlantic
        for i in range(rows):
            dfs(i, 0, pacific)
            dfs(i, cols - 1, atlantic)

        result = []

        for i in range(rows):
            for j in range(cols):
                if (i, j) in pacific and (i, j) in atlantic:
                    result.append([i, j])

        return result
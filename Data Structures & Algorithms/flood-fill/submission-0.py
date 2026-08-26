class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        so this does not seem too differnet to the other ones being done its just this time its 
        about changing the color and not numebrs exactly 

        it seems the color is a varibale but im not sure entirely how to change the color 

        beign with the very top left and if thats not a 1 then we stop and reutnr waht we have

        if it is then we have to do dfs for the neighboring and if its 1 then we change the color of it and then continue if not if its a 0 then we stop by color it seems to change the number to 2 

        ----

        so we begin at one color [sr][sc] then that has a color (number) 
        for everything adj that is the same (number) we have to change it to the new color 
        """
        original = image[sr][sc]
        if original == color:
            return image

        def dfs(sr, sc, original):
            image[sr][sc] = color
            if sr < len(image) - 1 and image[sr + 1][sc] == int(original):
                dfs(sr + 1,sc, original)
            if sr != 0 and image[sr - 1][sc] == int(original):
                dfs(sr - 1,sc, original)
            if sc < len(image[0]) - 1 and image[sr][sc + 1] == int(original):
                dfs(sr,sc + 1, original)
            if sc != 0 and image[sr][sc - 1] == int(original):
                dfs(sr,sc - 1, original)

        
        dfs(sr, sc, original)
        return image
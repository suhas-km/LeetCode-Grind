class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        ROWS, COLS = len(image), len(image[0])
        originalColor = image[sr][sc]

        # If the new color is the same as original, no need to do anything
        if originalColor == color:
            return image

        def dfs(sr, sc):
            # is out of bound or color check or not in visited
            if (sr >= ROWS or sr < 0) or (sc >= COLS or sc < 0) or ((sr,sc) in visited) or (image[sr][sc] != originalColor):
                return
            
            image[sr][sc] = color # change the color
            visited.add((sr,sc))

            dfs(sr+1, sc)
            dfs(sr, sc+1)
            dfs(sr-1, sc)
            dfs(sr, sc-1)

        dfs(sr,sc)
        return image
    
            

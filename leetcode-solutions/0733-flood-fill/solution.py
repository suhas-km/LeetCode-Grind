class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Get the original color at the starting position
        original_color = image[sr][sc]
        
        # If the new color is the same as original, no need to do anything
        if original_color == color:
            return image
        
        # Get dimensions
        rows, cols = len(image), len(image[0])
        
        def dfs(r, c):
            # Check if current position is valid and has original color
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                image[r][c] != original_color):
                return
            
            # Fill the current pixel with new color
            image[r][c] = color
            
            # Recursively fill all 4 adjacent pixels
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left
        
        # Start DFS from the given starting position
        dfs(sr, sc)
        return image
        
        

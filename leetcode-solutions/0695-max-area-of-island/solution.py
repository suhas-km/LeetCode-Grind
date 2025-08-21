class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0

        def dfs(r, c):
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or (r,c) in visited or grid[r][c] != 1:
                return 0
            
            visited.add((r,c))
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0 and (r,c) not in visited:
                    maxArea = max(maxArea, dfs(r, c))
        
        return maxArea

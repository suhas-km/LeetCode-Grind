class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # without set o(1) space
        # visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            # visited.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    count += 1
        return count

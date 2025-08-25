class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs
        ROWS, COLS = len(grid), len(grid[0])
        rotten = collections.deque()
        visited = set()
        freshOrange = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                if grid[r][c] == 1:
                    freshOrange += 1
                
        if freshOrange == 0:
            return 0
        
        directions = [(0, 1),(0, -1),(1, 0),(-1, 0)] # to be used to execute bfs calls
        level = -1 # because you dont want to increase the timer by 1 for last level rotten oranges
        
        while rotten:
            level += 1
            for i in range(len(rotten)):
                currRow, currCol = rotten.popleft()
                visited.add((currRow, currCol))
                for dx, dy in directions:
                    newRow = currRow + dx
                    newCol = currCol + dy
                    if 0 <= newRow < ROWS and 0 <= newCol < COLS and grid[newRow][newCol] == 1 and (newRow, newCol) not in visited:
                        grid[newRow][newCol] = 2
                        rotten.append((newRow, newCol))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return level

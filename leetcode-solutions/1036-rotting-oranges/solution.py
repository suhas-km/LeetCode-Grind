class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        freshOranges = 0
        rottenOranges = collections.deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshOranges += 1
                
                if grid[r][c] == 2:
                    rottenOranges.append((r, c))
        
        if freshOranges == 0:
            return 0
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        level = -1

        while rottenOranges:
            level += 1
            for i in range(len(rottenOranges)):
                curRow, curCol = rottenOranges.popleft()
                visited.add((curRow, curCol))
                for dx, dy in directions:
                    newRow = curRow + dx
                    newCol = curCol + dy
                    if 0 <= newRow < ROWS and 0 <= newCol < COLS and grid[newRow][newCol] == 1 and (newRow, newCol) not in visited:
                        grid[newRow][newCol] = 2
                        rottenOranges.append((newRow, newCol))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return level

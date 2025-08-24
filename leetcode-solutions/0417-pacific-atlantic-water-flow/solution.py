class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificVisited = set() # 
        atlanticVisited = set() # these sets know which index reaches to the ocean

        ROWS, COLS = len(heights), len(heights[0])
        
        def dfs(r, c, prevVal, currSet):
            if r >= ROWS or r < 0 or c < 0 or c >= COLS or (r,c) in currSet or heights[r][c] < prevVal:
                return
            
            currSet.add((r,c))
            dfs(r+1, c, heights[r][c], currSet)
            dfs(r-1, c, heights[r][c], currSet)
            dfs(r, c+1, heights[r][c], currSet)
            dfs(r, c-1, heights[r][c], currSet)

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    dfs(r,c,heights[r][c],pacificVisited) # pacific

                if r == ROWS - 1 or c == COLS - 1:
                    dfs(r,c,heights[r][c],atlanticVisited) # atlantic
        
        res = []
        for val in pacificVisited:
            if val in atlanticVisited:
                res.append(list(val))
        
        return res

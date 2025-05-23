class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #O(1) memory solution
        
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False # the extra variable to tell us if the first row is not zero, but well update it to True if needed
        
        # to determine which COLS need to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        
        # Then we zero out most of them
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # then we zero out the first column if we need to!
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
                
        # Again if we need to we will zero out the first row!
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

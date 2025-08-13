class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        flaggedRow = set()
        flaggedCol = set()

        for r in range(ROWS):
            for c in range(COLS):

                if matrix[r][c] == 0:
                    flaggedRow.add(r)
                    flaggedCol.add(c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if r in flaggedRow or c in flaggedCol:
                    matrix[r][c] = 0
        


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        ROWS, COLS = len(matrix), len(matrix[0])

        # transpose
        for r in range(ROWS):
            for c in range(r + 1, COLS):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        # reflect
        for r in range(ROWS):
            for c in range(COLS // 2):
                matrix[r][c], matrix[r][(COLS -1) - c] = matrix[r][(COLS -1) - c], matrix[r][c]
        # transpose + reflect
        return matrix

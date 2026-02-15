class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        # transpose starts
        # We only swap elements above the diagonal
        # c starts at r + 1 so we skip:
        # c == r (diagonal) because (r,r) swapping with itself is pointless
        # c < r (below diagonal) because those swaps would be duplicates
        for r in range(ROWS):
            for c in range(r + 1, COLS):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        # For each row, you swap left side with right side.
        # You only go up to n//2 because once you’ve swapped the first half, the second half is already done.
        # In general: mirror = last_index − column you are on

        for r in range(ROWS):
            for c in range(COLS // 2):
                matrix[r][c], matrix[r][(COLS - 1) - c] = matrix[r][(COLS - 1) - c], matrix[r][c]
        
        return matrix
        


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search on the rows first

        ROWS, COLS = len(matrix), len(matrix[0])
        topRow, botRow = 0, ROWS - 1

        # 
        while topRow <= botRow:
            midRow = (topRow + botRow) // 2

            if target > matrix[midRow][-1]:
                topRow = midRow + 1

            elif target < matrix[midRow][0]:
                botRow = midRow - 1
            
            else:
                # found the row
                break
            
        row = (topRow + botRow) // 2
        l, r = 0, COLS - 1

        while l <= r:
            m = (l + r) // 2

            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            
            else:
                return True
        
        return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Since the numbers are sorted we can perform binary search
        # 2 passes: 1st to find the right row to search and next to find if target is there
        # pass 1: O(log(m))
        # pass 2: O(log(n))
        # total time complexity: O(log(m + n))

        ROWS, COLS = len(matrix), len(matrix[0])
        
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row -1
            else:
                break
        
        if not (top <= bot): return False

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

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        gridCheck = defaultdict(set)
        rowCheck = defaultdict(set)
        colCheck = defaultdict(set)

        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c].isdigit():
                    val = board[r][c]

                    if val in rowCheck[r] or val in colCheck[c] or val in gridCheck[(r // 3, c // 3)]:
                        return False

                    rowCheck[r].add(val)
                    colCheck[c].add(val)
                    gridCheck[(r // 3, c // 3)].add(val)
        
        return True

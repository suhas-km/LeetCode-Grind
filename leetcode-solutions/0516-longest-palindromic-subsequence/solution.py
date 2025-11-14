class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1 = " " + s
        s2 = " " + s[::-1]
    
        ROWS, COLS = len(s1), len(s2)

        dp = [[0] * COLS for _ in range(ROWS)]
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if s1[r] == s2[c]:
                    dp[r][c] = dp[r-1][c-1] + 1
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])
        
        return dp[-1][-1]


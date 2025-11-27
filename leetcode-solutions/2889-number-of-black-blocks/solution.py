class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        blackCount = defaultdict(int)
        
        for x, y in coordinates:
            for dx in (0, -1):
                for dy in (0, -1):
                    r = x + dx
                    c = y + dy
 
                    if 0 <= r < m - 1 and 0 <= c < n - 1:
                        blackCount[(r, c)] += 1
        
        res = [0] * 5
        
        for _, val in blackCount.items():
            res[val] += 1

        totalNonZero = sum(res[1:])
        totalBlocks = (m - 1) * (n - 1)
        res[0] = totalBlocks - totalNonZero

        return res

        

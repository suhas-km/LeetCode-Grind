class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * n
        adjPairs = 0
        res = []

        for idx, color in queries:
            left = colors[idx - 1] if idx > 0 else 0
            right = colors[idx + 1] if idx < len(colors) - 1 else 0

            if colors[idx] != 0 and colors[idx] == right:
                adjPairs -= 1
            if colors[idx] != 0 and colors[idx] == left:
                adjPairs -= 1

            colors[idx] = color

            if colors[idx] == right:
                adjPairs += 1
            if colors[idx] == left:
                adjPairs += 1
            
            res.append(adjPairs)
        
        return res

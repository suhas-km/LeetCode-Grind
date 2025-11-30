class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * n
        adjPairs = 0
        res = []

        for i, color in queries:
            left = colors[i - 1] if i > 0 else 0
            right = colors[i + 1] if i < len(colors) - 1 else 0

            if colors[i] != 0 and colors[i] == right:
                adjPairs -= 1
            if colors[i] != 0 and colors[i] == left:
                adjPairs -= 1
            
            colors[i] = color

            if colors[i] == right:
                adjPairs += 1
            
            if colors[i] == left:
                adjPairs += 1
            
            res.append(adjPairs)
        
        return res

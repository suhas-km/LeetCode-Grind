class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        origin - (0,0)

        R- 
        L- 
        U-
        D- 

        """

        initial = [0,0]

        for move in moves:
            if move == 'U':
                initial[1] += 1
            elif move == 'D':
                initial[1] -= 1
            elif move == 'R':
                initial[0] += 1
            else:
                initial[0] -= 1
        
        return initial == [0,0]

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        """
        scoreCard = []
        # total = 0

        for ch in operations:
            if ch == "+":
                scoreCard.append(scoreCard[-1] + scoreCard[-2])
            elif ch == "D":
                scoreCard.append(2*scoreCard[-1])
            elif ch == "C":
                scoreCard.pop()
            else:
                scoreCard.append(int(ch))
        
        return sum(scoreCard)


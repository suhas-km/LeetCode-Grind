class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        # Check if all suits are the same (flush condition)
        if len(set(suits)) == 1:
            return "Flush"
        
        # Count the frequency of each rank
        rank_count = Counter(ranks)
        max_countR = max(rank_count.values())
        
        # Check for three of a kind
        if max_countR >= 3:
            return "Three of a Kind"
        # Check for pair
        elif max_countR == 2:
            return "Pair"
        # Otherwise, it's a high card
        else:
            return "High Card"

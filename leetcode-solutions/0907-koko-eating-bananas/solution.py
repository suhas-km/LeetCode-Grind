# Problem: Find the minimum eating speed 'k' such that all bananas in 'piles' can be eaten within 'h' hours.
# Approach: Binary search over possible speeds (1 to max pile), and simulate time taken for each guess.

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # range of possible "k"
        res = r

        while l <= r:
            m = (l + r) // 2
            timeTaken = 0

            for pile in piles:
                timeTaken += math.ceil(pile/m)    # calculate time taken for each pile
            
            if timeTaken <= h:
                res = min(m, res)
                r = m - 1

            else:
                l = m + 1
            
        return res

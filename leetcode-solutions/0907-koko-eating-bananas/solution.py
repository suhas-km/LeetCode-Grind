# Problem: Find the minimum eating speed 'k' such that all bananas in 'piles' can be eaten within 'h' hours.
# Approach: Binary search over possible speeds (1 to max pile), and simulate time taken for each guess.

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)  # Search space: 1 to the largest pile
        res = r  # Start with the max possible speed as the worst case

        while l <= r:
            k = (l + r) // 2  # Midpoint guess for eating speed
            hours = 0

            # Calculate total hours needed at speed k
            for p in piles:
                hours += math.ceil(p / k)

            # If possible within h hours, try to lower speed
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:  # Too slow, need to increase speed
                l = k + 1

        return res  # Minimum valid speed found


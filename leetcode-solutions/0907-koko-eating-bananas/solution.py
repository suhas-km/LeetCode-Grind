class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            totalTime = 0

            # calculate how many hours it takes to complete piles
            for pile in piles:
                totalTime += math.ceil(pile/m)
            
            if totalTime > h:
                l = m + 1
            
            elif totalTime <= h:
                r = m - 1
                res = m
        
        return res

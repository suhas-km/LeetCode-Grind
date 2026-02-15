class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = float("-inf")
        curProfit = float("-inf")

        buyPrice = prices[0]

        for price in prices:
            if price < buyPrice:
                # buying cheap is the goal
                buyPrice = price
            
            curProfit = price - buyPrice
            maxProfit = max(maxProfit, curProfit)

        return maxProfit


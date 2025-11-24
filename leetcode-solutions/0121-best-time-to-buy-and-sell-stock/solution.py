class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        curProfit = 0
        buyPrice = prices[0]

        for price in prices:
            if price < buyPrice:
                buyPrice = price

            curProfit = price - buyPrice

            # curProfit = max(curProfit, profit)
            maxProfit = max(maxProfit, curProfit)
        
        return maxProfit

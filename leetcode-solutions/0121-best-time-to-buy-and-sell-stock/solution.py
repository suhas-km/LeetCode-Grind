class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0  # Initialize profit as 0 initially

        for price in prices:
            if price < minPrice:
                minPrice = price  # Update min price

            maxProfit = max(maxProfit, price - minPrice)  # Calculate profit

        return maxProfit

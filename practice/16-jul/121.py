class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minPrice = float('inf')

        for price in prices:
            maxP = max(maxP, price - minPrice)
            minPrice = min(minPrice, price)

        return maxP 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 存最小的buy和最大的profit
        maxProfit = 0
        minPrice = prices[0]
        for price in prices:
            maxProfit = max(maxProfit, price - minPrice )
            minPrice = min(minPrice,price)
        return maxProfit 
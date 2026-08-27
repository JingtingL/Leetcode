class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we know the buy date always have to be on the left of the sell date
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            
            if max_profit < price - min_price:
                max_profit = price - min_price
            
        return max_profit

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # determine the best profit I can make
        result = 0
        buy_price = float('inf')
        
        for curr in range(0,len(prices)):
            result = max(prices[curr] - buy_price, result)

            if prices[curr] < buy_price:
                buy_price = prices[curr]
        
        return result

        
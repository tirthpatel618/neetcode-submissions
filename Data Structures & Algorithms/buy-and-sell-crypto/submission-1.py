class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 pointers
        # treat i as your sell price and iterate. 

        buy = 0
        sell = 1
        maxP = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]: # sell price greater therefore a profit can be made
                profit = prices[sell] - prices[buy]
                maxP = max(maxP, profit) 
            else:
                buy = sell #if the sell price is less than buy price, that should become the new buy price 
            sell += 1
        return maxP

        
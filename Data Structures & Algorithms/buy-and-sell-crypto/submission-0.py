class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        max_profit = 0
        
        l = 0
        curr_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[l]
            if profit > curr_profit: 
                curr_profit = profit
            elif profit < 0:
                l = i
            
            if curr_profit > max_profit:
                max_profit = curr_profit

        return max(0, max_profit)
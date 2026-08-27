class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        total_profit = 0


        while r < (len(prices)):
            if prices[l] < prices[r]:
                total_profit = max(total_profit, prices[r] - prices[l])
                
            else:
                l = r
            r+= 1
            
        return total_profit

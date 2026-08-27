class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        maxprofit = 0

        for r in range(len(prices)):
            maxprofit = max(maxprofit, (prices[r] - prices[l]))
            
            while prices[l] > prices[r] and l < r:
                l+=1
        return maxprofit
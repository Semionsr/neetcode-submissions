class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l = 0
        r = 1
        for r in range(len(prices)):

            while prices[l] >= prices[r] and l < r:
                l += 1

            res = max(prices[r]- prices[l], res)
        
        return res

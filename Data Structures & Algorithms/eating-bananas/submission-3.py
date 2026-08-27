class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1, max(piles)
        res = float("infinity")

        while l <= r:
            total = 0
            m = (l+r)//2
            
            for i in range(len(piles)):
                total += math.ceil(float(piles[i])/m)

            
            if total > h:
                l = m +1
            else:
                r = m -1
                res = min(res, m)
        return res



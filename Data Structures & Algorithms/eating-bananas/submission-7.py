class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)-1

        #total = 0
        res = max(piles)

        while l <= r:
            k = (l+r)//2
            total  = 0
            for i, p in enumerate(piles):
                total += math.ceil(float(p)/k)

            if total > h:
                l = k + 1
                
            else:
                res = min(res, k)
                r = k - 1

        return res

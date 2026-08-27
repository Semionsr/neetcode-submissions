class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1, max(piles)
        res = max(piles)


        while l <= r:
            k = (l+r)//2
            total = 0
            


            for i, p in enumerate(piles):
                print(p)
                print(k)
                total += math.ceil(float(p)/k)
            
            if total > h:
                l = k + 1

            else:
                res = min(k, res)
                r = k - 1
        return res




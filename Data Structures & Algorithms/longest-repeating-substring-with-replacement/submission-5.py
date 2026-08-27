class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        total = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            total = max(total, count[s[r]])


            while (r- l +1) - total > k:
                count[s[l]] -= 1
                l += 1
                
            res = max(r-l+1, res)
        return res


                

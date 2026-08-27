class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        checker = {}
        res = 0
        
        count = 0


        for r in range(len(s)):
            checker[s[r]] = 1 + checker.get(s[r], 0)
            count = max(count, checker[s[r]])

            
            while (r-l+1 - count > k):
                checker[s[l]] -= 1
                l += 1

            res = max(res, r -l + 1)

        
        return res
                
 

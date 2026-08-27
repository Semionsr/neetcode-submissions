class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checker = set()

        l = 0
        maxsub = 0

        for r in range(len(s)):
            
            

            while s[r] in checker and checker:
                checker.remove(s[l])
                l += 1
            maxsub = max(maxsub, (r-l+1))
            
            checker.add(s[r])

        return maxsub
            


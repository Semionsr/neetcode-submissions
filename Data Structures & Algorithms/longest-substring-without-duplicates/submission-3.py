class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = set()
        l = 0
        total = 0

        for r in range(len(s)):
            while s[r] in substr:
                substr.remove(s[l])
                l += 1
            substr.add(s[r])
            total = max(total, r-l+1)
        return total
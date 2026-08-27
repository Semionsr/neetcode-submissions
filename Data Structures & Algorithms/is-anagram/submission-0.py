class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        total_s = {}
        total_t = {}
        for i in range(len(s)):
            total_s[s[i]] = 1 + total_s.get(s[i],0)
            total_t[t[i]] = 1 + total_t.get(t[i],0)
        for c in total_s:
            if total_s[c] != total_t.get(c, 0):
                return False
        return True
            

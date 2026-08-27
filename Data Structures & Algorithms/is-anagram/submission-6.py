class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       if len(s) != len(t):
            return False
       
       checker1 = {}
       checker2 = {}

       for i in range(len(s)):
        checker1[s[i]] = 1 + checker1.get(s[i],0)
        checker2[t[i]] = 1 + checker2.get(t[i],0)

       if checker1 == checker2:
        return True
       return False
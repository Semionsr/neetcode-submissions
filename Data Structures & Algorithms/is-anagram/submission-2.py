class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        checker1 = {}
        checker2 = {}

        for i in s:
            checker1[i] = 1 + checker1.get(i, 0)
        
        for i in t:
            checker2[i] = 1 + checker2.get(i, 0)
        
        if checker1 == checker2:
            return True
        return False

        
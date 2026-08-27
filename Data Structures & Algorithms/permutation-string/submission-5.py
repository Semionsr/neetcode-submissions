class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        checker1 = [0] * 26
        checker2 = [0] * 26

        for c in range(len(s1)):
            checker1[ord(s1[c]) - ord('a')] += 1
            checker2[ord(s2[c]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if checker1[i] == checker2[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            checker2[ord(s2[r]) - ord('a')] += 1
            if checker1[ord(s2[r]) - ord('a')] == checker2[ord(s2[r]) - ord('a')]:
                matches += 1
            elif checker1[ord(s2[r]) - ord('a')]+1 == checker2[ord(s2[r]) - ord('a')]:
                matches -= 1
            
            checker2[ord(s2[l]) - ord('a')] -= 1
            if checker1[ord(s2[l]) - ord('a')] == checker2[ord(s2[l]) - ord('a')]:
                matches += 1
            elif checker1[ord(s2[l]) - ord('a')]-1 == checker2[ord(s2[l]) - ord('a')]:
                matches -= 1
            l += 1
        
        return matches == 26

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = 0
        checker = {}

        res = 0

        l = 0
        for r in range(len(s)):
            checker[s[r]] = 1 + checker.get(s[r], 0)
            frequency = max(checker[s[r]], frequency)

            while (r-l+1 - frequency > k):
                checker[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)

        return res

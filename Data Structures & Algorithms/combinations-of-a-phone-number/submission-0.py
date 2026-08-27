class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        checker = { "2" : "abc",
                    "3" : "def",
                    "4" : "ghi",
                    "5" : "jkl",
                    "6" : "mno",
                    "7" : "pqrs",
                    "8" : "tuv",
                    "9" : "wxyz"}
        res = []
        
        def dfs(i,stringer):
            if len(stringer) == len(digits):
                res.append(stringer)
                return

            if digits[i] in checker:
                for c in checker[digits[i]]:
                    dfs(i + 1, stringer + c)
        
        if digits:
            dfs(0,"")


        return res


        
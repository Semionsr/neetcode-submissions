class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        openN, closedN = 0 , 0
        stack = []
        res = []

        def checker(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                checker(openN + 1,closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                checker(openN,closedN + 1)
                stack.pop()
        
        checker(openN,closedN)
        return res
        




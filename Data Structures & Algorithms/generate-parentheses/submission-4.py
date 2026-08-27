class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        openn, closedn = 0, 0

        
        stack = []
        res = []
        def checker(openn, closedn):
            if openn == closedn == n:
                res.append("".join(stack))
                return

            if openn < n:
                stack.append("(")
                checker(openn+1,closedn)
                stack.pop()
            if closedn < openn:
                stack.append(")")
                checker(openn,closedn+1)
                stack.pop()
        
        checker(openn,closedn)
        return res
            




            

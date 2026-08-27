class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        checker = {')': '(', '}' : '{', ']' : '['}

        for i in range(len(s)):
            
            if stack and s[i] in checker and stack[-1] == checker[s[i]]:
                stack.pop()
            else:
                stack.append(s[i])

        if not stack: 
            return True 
        else: 
            return False

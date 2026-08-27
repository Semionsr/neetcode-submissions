class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] == "+":
                total = (stack.pop() + stack.pop())
                stack.append(total)
            elif tokens[i] == "-":
                total = ( - stack.pop() + stack.pop())
                stack.append(total)
            elif tokens[i] == "*":
                total = (stack.pop() * stack.pop())
                stack.append(total)
            elif tokens[i] == "/":
                total = int(float(1/(stack.pop()) * stack.pop()))
                stack.append(total)
            else:
                stack.append(int(tokens[i]))

        return stack[0]
        
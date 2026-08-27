class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        new = 0

        for c in tokens:
            stack.append(c)
            if c == "+":
                stack.pop()
                first_val = int(stack.pop())
                second_val = int(stack.pop())
                new = first_val + second_val
                stack.append(new)
            if c == "-":
                stack.pop()
                first_val = int(stack.pop())
                second_val = int(stack.pop())
                new = second_val - first_val
                stack.append(new)

            if c == "*":
                stack.pop()
                first_val = int(stack.pop())
                second_val = int(stack.pop())
                new = first_val * second_val
                stack.append(new)

            if c == "/":
                stack.pop()
                first_val = int(stack.pop())
                second_val = int(stack.pop())
                new = second_val / first_val
                stack.append(new)
        return int(stack[-1])



        
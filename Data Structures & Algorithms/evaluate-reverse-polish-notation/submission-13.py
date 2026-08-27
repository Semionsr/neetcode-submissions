class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        #res = []

        for i in range(len(tokens)):
            if stack and tokens[i] == "+":
                stack.append(stack.pop()+stack.pop())

            elif stack and tokens[i] == "-":
                stack.append(-stack.pop()+stack.pop())

            elif stack and tokens[i] == "*":
                stack.append(stack.pop()*stack.pop())

            elif stack and tokens[i] == "/":
                total = int(float(1/(stack.pop()) * stack.pop()))
                stack.append(total)
            
            else:
                stack.append(int(tokens[i]))

        return stack[0]
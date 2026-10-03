class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # ["1","2","+","3","*","4","-"]
        # stack 

        stack = []

        for i in range(len(tokens)):
            if tokens[i] != '+' and tokens[i] != '-' and tokens[i] != '*' and tokens[i] != '/':
                stack.append(int(tokens[i]))
            
            if tokens[i] == '+':
                val1, val2 = stack.pop(), stack.pop()
                val3 = val1 + val2
                stack.append(val3)

            if tokens[i] == '-':
                val1, val2 = stack.pop(), stack.pop()
                val3 = val2 - val1
                stack.append(val3)
            

            if tokens[i] == '*':
                val1, val2 = stack.pop(), stack.pop()
                val3 = val1 * val2
                stack.append(val3)

            if tokens[i] == '/':
                val1, val2 = stack.pop(), stack.pop()
                val3 = int(val2 / val1)
                stack.append(val3)


        return stack[0] if stack else 0











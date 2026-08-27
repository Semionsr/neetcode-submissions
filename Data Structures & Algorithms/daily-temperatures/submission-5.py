class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # index and temperature
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
                
            while stack and stack[-1][1] < temperatures[i]:
                print(stack[-1][1])
                stackind, stacktemp = stack.pop()
                res[stackind] = (i-stackind)
            stack.append((i, temperatures[i]))

        return res

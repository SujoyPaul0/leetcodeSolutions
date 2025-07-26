class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
                if t == "+":
                    num1 = stack.pop() 
                    num2 = stack.pop() 
                    res = int(num2) + int(num1)
                    stack.append(res)

                elif t == "-":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    res = int(num2) - int(num1)
                    stack.append(res)

                elif t == "*":
                    num1 = stack.pop() 
                    num2 = stack.pop() 
                    res = int(num2) * int(num1)
                    stack.append(res)

                elif t == "/":
                    num1 = stack.pop()
                    num2 = stack.pop() 
                    res = int(num2) / int(num1)
                    stack.append(int(res))

                else:
                    stack.append(t)

        return int(stack[0])
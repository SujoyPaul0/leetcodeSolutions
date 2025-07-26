class Solution:
    def evaluation(self, num1, num2, operator) -> int:
        if operator == "+": 
            res = int(num2) + int(num1)
        elif operator == "-":
            res = int(num2) - int(num1)
        elif operator == "*":
            res = int(num2) * int(num1)
        else:
            res = int(num2) / int(num1)
        
        return res

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])

        for t in tokens:
                if t in operators:
                    num1 = stack.pop() 
                    num2 = stack.pop() 
                    res = self.evaluation(num1, num2, t)
                    stack.append(res)
                else:
                    stack.append(t)

        return int(stack[0])
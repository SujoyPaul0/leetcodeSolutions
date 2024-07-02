class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        
        for op in operations:
            if op == "C":
                if res:
                    res.pop()
            elif op == "D":
                if res:
                    res.append(2 * res[-1])
            elif op == "+":
                if len(res) >= 2:
                    res.append(res[-1] + res[-2])
            else:
                res.append(int(op))
        
        return sum(res)

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        res = ''
        for ch in s:
            if ch != '*':
                stack.append(ch)
            elif ch == '*' and stack:
                stack.pop()

        while stack:
            res = stack.pop() + res
        
        return res
                

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == '*':
                stack.pop()
            else:
                stack.append(ch)

        res = ""
        for ch in stack:
            res += ch

        return res
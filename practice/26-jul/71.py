class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        pArr = path.split('/')

        for p in pArr:
            if p == "" or p == '.':
                continue
            elif p == ".." and stack:
                stack.pop()
            elif p == ".." and not stack:
                continue
            else:
                stack.append(p)

        str = '/'
        for i in range(len(stack)):
            str += stack[i]
            str += '/'

        if len(str) > 1:
            return str[:-1]
        else:
            return str
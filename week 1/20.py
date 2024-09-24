class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if len(s)==1:
            return False
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            elif ch in ')}]':
                if len(stack)==0:
                    return False
                if stack[-1]=='(' and ch==')':
                    stack.pop(-1)
                elif stack[-1]=='{' and ch=='}':
                    stack.pop(-1)
                elif stack[-1]=='[' and ch==']':
                    stack.pop(-1)
                else:
                    return False
        return len(stack)==0
'''
Input: path = "/home/user/Documents/../Pictures"
Output: "/home/user/Pictures"
Explanation:
A double period ".." refers to the directory up a level (the parent directory).
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        # Create Stack
        stack = []
        curr = ""

        # iterate through path + "/"
        for c in path + "/":
            if c == "/":
                if curr == "..":
                    if stack: stack.pop()
                elif curr != '.' and curr != "":
                    stack.append(curr)
                curr = ""
            else:
                curr += c
        return "/" +  "/".join(stack)
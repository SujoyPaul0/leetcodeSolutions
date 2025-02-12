'''
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Input: s = "a"
Output: [["a"]]
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = [] # stores the partition

        def dfs(i):
            # if we reached the end then it is the res
            if i >= len(s):
                res.append(part.copy())
                return
                # j in range i to end
            for j in range(i, len(s)):
                # check if string is palindrome
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
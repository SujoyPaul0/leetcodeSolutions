class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if not s: 
            return True

        if not t:
            return False

        i, j = 0, 0

        while i < len(s) and j < len(t):
            if i == len(s)-1 and s[i] == t[j]:
                return True
            elif s[i] != t[j]:
                j += 1
            else:
                i += 1
                j += 1
        
        return False
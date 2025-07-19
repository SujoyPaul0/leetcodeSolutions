class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t or len(s) > len(t):
            return False
        
        sInd = 0
        sLen = len(s)

        for ch in t:
            if sInd >= sLen -1 and ch == s[sInd]:
                return True
            elif ch == s[sInd]:
                sInd += 1
        
        return False
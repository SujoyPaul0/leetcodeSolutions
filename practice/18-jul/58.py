class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        resArray = s.split()
        s = resArray[-1]
        return len(s)
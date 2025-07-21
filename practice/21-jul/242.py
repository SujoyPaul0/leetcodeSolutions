class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = Counter(s)
        tCount = Counter(t)

        if len(s) != len(t):
            return False

        for ch_s in s:
            if sCount[ch_s] != tCount[ch_s]:
                return False
        
        return True
         
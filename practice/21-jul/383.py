import string
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hMap = {ch: 0 for ch in string.ascii_lowercase}
        
        for ch in ransomNote:
            hMap[ch] += 1

        for ch in magazine:
            if ch in hMap:
                hMap[ch] -= 1

        for key, value in hMap.items():
            if value > 0:
                return False
        return True            
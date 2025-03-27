'''
Input: ransomNote = "a", magazine = "b"
Output: false
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        st1, st2 = Counter(ransomNote), Counter(magazine)
        # Check if the intersection of both Counters is equal to st1
        if st1 & st2 == st1: # Using bitwise AND to get the minimum frequency for common keys
            return True
        return False
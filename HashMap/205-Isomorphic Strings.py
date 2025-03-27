'''
Input: s = "egg", t = "add"
Output: true
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # If two strings follow the same pattern of first occurrences, they are isomorphic.
        # Lists to store the first index of each character in s and t
        map1 = []
        map2 = []

        # Loop through each character in s and store the index of its first occurence
        for idx in s:
            map1.append(s.index(idx)) # s.index(idx) returns the first occurence index of id
        
        # same for t
        for idx in t:
            map2.append(t.index(idx))
        
        # If both lists are identical, s and t follow the sam pattern -> thr are isomorphic
        if map1 == map2:
            return True
        return False
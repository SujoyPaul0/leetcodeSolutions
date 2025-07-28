class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sSet = set()
        length = 0
        l = 0

        for r in range(len(s)):
            while s[r] in sSet:
                sSet.remove(s[l])
                l += 1
            sSet.add(s[r])
            length = max(length, r - l + 1)

        return length
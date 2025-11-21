class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxWindow = 0
        l = 0
        hMap = collections.defaultdict(int)
        
        for r in range(len(s)):
            if s[r] not in hMap:
                hMap[s[r]] += 1
            else:
                maxWindow = max(maxWindow, r - l)
                if s[l] == s[r]:
                    l += 1
                else:
                    while s[l] != s[r]:
                        hMap.pop(s[l])
                        l += 1
                    l += 1

        return max(maxWindow, len(s) - l)
                


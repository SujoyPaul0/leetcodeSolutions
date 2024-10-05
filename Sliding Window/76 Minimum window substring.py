'''Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        # making two hashmaps for coun in t and window
        # window takes care of the elements we are checking
        countT, window = {}, {}

        # for every chr in t update count of chr
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # have to see the elements we have in cur window which are in t
        # need is the count of elements of chr in t
        have, need = 0, len(countT)

        # res stores indexes of window's start and end
        # resLen is the length of window 
        res, resLen = [-1, -1], float("infinity")
        l = 0

        # initiate right pointer
        for r in range(len(s)):
            # store chr at in c
            c = s[r]
            # update count of c in window
            window[c] = 1 + window.get(c, 0)

            # check if we need the chr or not and
            # also check their count
            if c in countT and window[c] == countT[c]:
                # if so update have count
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window and update count of chr in window
                window[s[l]] -= 1
                # now check again if chr in countT and count of chr
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        # update result
        l, r = res
        # return string of least length
        return s[l: r + 1] if resLen != float("infinity") else ""
        
            

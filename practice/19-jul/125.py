class Solution:
    def isPalindrome(self, s: str) -> bool:
        sArray = []
        s.strip()

        for ch in s:
            if ch.isalnum():
                sArray.append(ch.lower())

        l, r = 0, len(sArray) - 1
        while l < r:
            if sArray[l] != sArray[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
            
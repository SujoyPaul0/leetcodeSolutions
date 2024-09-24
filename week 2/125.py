class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        s_list = []
        for c in s:
            if c.isalnum():
                s_list.append(c.lower())  

        l, r = 0 , len(s_list) - 1
        while l < r:
            if s_list[l] != s_list[r]:
                return False
            l += 1
            r -= 1

        return True
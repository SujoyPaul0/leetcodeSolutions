'''
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

 

Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"
'''

class Solution:
    def toLowerCase(self, s: str) -> str: 
        ans = ""
        for c in s:
            n = ord(c)
            ans += chr(n+32) if n > 64 and n < 91 else c
        return ans

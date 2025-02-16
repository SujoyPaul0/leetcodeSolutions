'''
Example 1:

Input: s = "aaabaaa", k = 3

Output: true

Explanation:

The substring s[4..6] == "aaa" satisfies the conditions.

It has a length of 3.
All characters are the same.
The character before "aaa" is 'b', which is different from 'a'.
There is no character after "aaa".
Example 2:

Input: s = "abc", k = 2

Output: false©leetcode
'''

class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)

        # Edge case: If k is greater than the length of s, return False
        if k > n:
            return False

        for i in range(n - k + 1):
            # Check if the substring of length k consits of one distince character
            if len(set(s[i: i + k])) == 1:
                # Check the boundary conditions
                if (i == 0 or s[i - 1] != s[i]) and (i + k == n or s[i + k] != s[i]):
                    return True

        return False

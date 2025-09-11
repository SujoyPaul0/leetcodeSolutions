'''
Example 2:
Input: s = "icodeinpython", spaces = [1,5,7,9]
Output: "i code in py thon"
Explanation:
The indices 1, 5, 7, and 9 correspond to the underlined characters in "icodeinpython".
We then place spaces before those characters.

Example 3:
Input: s = "spacing", spaces = [0,1,2,3,4,5,6]
Output: " s p a c i n g"
Explanation:
We are also able to place spaces before the first character of the string.
'''
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i,j = 0,0
        res = ''

        while j < len(s):
            if i < len(spaces) and j == spaces[i]:
                res += ' '
                i += 1
            res += s[j]
            j += 1
            

        return res

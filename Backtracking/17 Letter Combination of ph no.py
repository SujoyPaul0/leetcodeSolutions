'''
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""
Output: []
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = { "2": "abc",
                        "3": "def",
                        "4": "ghi",
                        "5": "jkl",
                        "6": "mno",
                        "7": "qprs",
                        "8": "tuv",
                        "9": "wxyz"}

        def backtrack(i, curStr):
            # if curStr length and digits length is same
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            # loop through each chr in digits[i]
            for c in digitToChar[digits[i]]:
                # and call backtrack on next digit to also add chr to curStr
                backtrack(i+1, curStr + c)
        # only if digit is not empty
        if digits:
            backtrack(0, "")

        return res
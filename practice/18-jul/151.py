class Solution:
    def reverseWords(self, s: str) -> str:
        resArr = s.split()
        res = ''

        for i in range(len(resArr) - 1, -1, -1):
            res += resArr[i]
            if i != 0:
                res += ' '
        
        return res
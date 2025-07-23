class Solution:
    def reverseWords(self, s: str) -> str:
        sArray = s.split()

        res = ""
        
        for i in range(len(sArray)-1, -1, -1):
            res += sArray[i]
            if i != 0:
                res += " "

        return res


        
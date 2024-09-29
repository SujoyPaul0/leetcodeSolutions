'''
String Encode and Decode
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
'''

class Solution:

    def encode(self, strs):
        # iterate through the list
        s = ''
        for i in strs:
        # add all the elements to an empty string variable
            s += i
        # separate each element whith $
            s += '$'
        # return the string
        return s

    def decode(self, s: str):
        # iterate through the string
        st = []
        decodedString = ''
        if len(s) > 0:
            for i in range(len(s)):
            # we separate the string by $
                if s[i] != '$':
                  decodedString += s[i]
                else:
                  st.append(decodedString)
                  decodedString = ''
        return st
                  
            
        
      
solution = Solution()
print(solution.encode(["we","say",":","yes"]))
print(solution.decode('we$say$:$yes$'))


##########################################################


class Solution:

    def encode(self, strs: list[str]) -> str:
        # Using join to efficiently concatenate strings with '$' as separator
        return '$'.join(strs) + '$'

    def decode(self, s: str) -> list[str]:
        # If the input string is empty, return an empty list
        if not s:
            return []
        
        # Splitting by '$' to decode, ignoring the last empty element
        return s.split('$')[:-1]

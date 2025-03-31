'''
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
'''
class Solution:
    def calculate(self, s: str) -> int:
        # Current number being formed
        cur = 0  
        # Result of the expression so far
        res = 0  
        # Sign of the current number (1 for positive, -1 for negative)
        sign = 1  
        # Stack to handle parentheses
        stack = []  

        # Iterate through each character in the string
        for char in s:
            if char.isdigit():
                # Build the current number (handles multi-digit numbers)
                cur = cur * 10 + int(char)
            
            elif char in ['+', '-']:
                # Add the previous number to result with its sign
                res += sign * cur  
                # Update sign for next number
                sign = 1 if char == '+' else -1  
                # Reset current number
                cur = 0  
            
            elif char == "(":
                # Push current result onto stack (stores previous result)
                stack.append(res)
                # Push current sign onto stack (stores previous sign)
                stack.append(sign)
                # Reset result and sign for the new subexpression inside parentheses
                sign = 1  
                res = 0  
            
            elif char == ")":
                # Add the last number before closing parentheses
                res += sign * cur  
                # Multiply by the sign before the parentheses
                res *= stack.pop()  
                # Add back the previous result before the parentheses
                res += stack.pop()  
                # Reset current number
                cur = 0  
        
        # Add the last number in the expression
        return res + sign * cur  

'''
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

Output: 3

Explanation:

The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
'''

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # making pair of position and speed
        pair = [[p, s] for p, s in zip(position, speed)]

        # store time to the stack
        stack = []
        for p, s in sorted(pair)[::-1]: # Reverse sorted order
            stack.append((target- p) / s) # append time to reach target
            # check if two time collides if so the pop the smallest
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
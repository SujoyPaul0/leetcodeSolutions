'''
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0 # to keep count of visited node
        stack = [] # stack to store nodes whose branch we are visiting
        cur = root # cur to keep track of ptr

        while cur or stack:
            while cur: # while cur visiting is not null
                stack.append(cur) # append cur to stack
                cur = cur.left # go to left of cur

            cur = stack.pop() # we got out of while loop so curr was null now we backtrack and change cur
            n += 1 # each time we pop we count cause we poping in increasing order
            if n == k: # this always executes as there will be k nodes
                return cur.val # cur node value is output
            cur = cur.right # if not we go to right sub-tree and try again


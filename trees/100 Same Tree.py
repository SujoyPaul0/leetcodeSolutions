'''
Input: p = [1,2,3], q = [1,2,3]
Output: true
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # check if p and q empty
        if not p and not q:
            return True
        # if p and q has same node val
        if p and q and p.val == q.val:
            # call the fun recursively for left and right subtree
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # else false
        return False
        
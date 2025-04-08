'''
Input: root = [1,2,2,3,4,4,3]
Output: true
Input: root = [1,2,2,null,3,null,3]
Output: false
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # fun for checkig symmetry
        def is_mirror(n1, n2): # n1: left, n2: right
            # if left and right is Null
            # we reached end
            if not n1 and not n2:
                return True
            # if one of n1, n2 is null
            # it's asymmetric 
            if not n1 or not n2:
                return False

            # check n1, n2 val ^ call mirror fun recursively
            # with left and right, then right and left
            return n1.val == n2.val and is_mirror(n1.left, n2.right) 
            and is_mirror(n1.right, n2.left)

        return is_mirror(root.left, root.right)
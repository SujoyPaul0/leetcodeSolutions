'''
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root

        while cur:
            if cur.left:
            # Find the rightmost node of the left subtree
                prev = cur.left
                while prev.right:
                    # Traverse to the rightmost node
                    prev = prev.right

                # Rewire the connections
                # attach the original right subtree to the rightmost node
                prev.right = cur.right
                
                # Move the left subtree to the right
                cur.right = cur.left

                # set the left child to None
                cur.left = None
            
            # Move on to the next node (which is now cur.right)
            cur = cur.right

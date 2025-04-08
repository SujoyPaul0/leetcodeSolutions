'''
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # if inorder is null: return None
        if not inorder:
            return None
        # root is last of postorder
        root = TreeNode(postorder.pop())
        # get index of root in inorder
        idx = inorder.index(root.val)
        # right will be inorder right after index upto end
        # and postorder itself after poping root
        root.right = self.buildTree(inorder[idx+1:], postorder)
        # left will be inorder start to index 
        # and postorder itself after poping root
        root.left = self.buildTree(inorder[:idx], postorder)
        return root
'''
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder, inorder is null: return None
        if not preorder or not inorder:
            return None
        # root is always the first of preorder
        root = TreeNode(preorder[0])
        # get index of root on which we will
        # create sublist of preorder and inorder
        # to pass them recursively in the buildTree
        mid = inorder.index(preorder[0])
        # left is right upto mid(index) in preorder
        # and upto mid-index in inorder 
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # right is from mid-index + 1 upto end in preorder
        # and from mid-index + 1 to end in inorder
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
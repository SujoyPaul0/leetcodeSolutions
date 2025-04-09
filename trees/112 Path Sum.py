'''
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # if root is null its false
        if not root:
            return False
        # if left and right of root exist
        if not root.left and not root.right:
            # check if target == root
            return targetSum == root.val
            
        # check left and right sum recursively by substracting
        # root val each time from target
        left_sum = self.hasPathSum(root.left, targetSum - root.val)
        right_sum = self.hasPathSum(root.right, targetSum - root.val)

        # return if left or right is true
        return left_sum or right_sum
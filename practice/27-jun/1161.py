# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        max_level = 1
        cur_level = 1
        max_sum = root.val

        while q:
            level_sum = 0
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                level_sum += node.val
                if node.right: q.append(node.right)
                if node.left: q.append(node.left)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = cur_level
            cur_level += 1

        return max_level


'''
Binary Tree Level Order Traversal

every node level is one list
each of the sublist to be put in one list
and the algo to do this is BFS
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] # To store the sublists in this list
        
        q = collections.deque() # Initiate queue in py
        q.append(root)
        
        while q: # while q is not empty
          qLen = len(q)
          level = [] # the list for the levels
          
          for i in range(qLen): # iterating by length of q
            node = q.popleft() # node is left poped
            if node: # if node is nonempty
              level.append(node.val) # level = [node]
              q.append(node.left) # q = [left]
              q.append(node.right) # q = [left, right]
          if level:
            res.append(level) # res = [level]
            
        return res
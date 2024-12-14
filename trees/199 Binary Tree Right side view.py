# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = [] # Result list
        q = collections.deque([root]) # queue with initial value of the root

        while q: # while queue is not empty
            rightSide = None # rightside value is initiated with none
            qLen = len(q)

            for i in range(qLen): # iterate of range len(q)
                node = q.popleft() # node is popped value from left of q which is root
                if node: # if node is not null
                    rightSide = node # rightside value is node now
                    q.append(node.left) # as we know node is not null we can append left child
                    q.append(node.right) # and also right child

            if rightSide: # if rightside is not null
                res.append(rightSide.val) # right side value appended in result

        return res
      
      
      '''
      runing an example
      '''
  input = [1,2,3,4,null,null,null,5]
      
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = [] # res = []
        q = collections.deque([root]) # q = [1] ## q = [3, 2]; [Null, Null, 2]

        while q: # True; true; true
            rightSide = None # rightSide = None, None, None
            qLen = len(q) # qLen = 1, 2, 1

            for i in range(qLen): # i in range(1); i in range(2), i in range(1)
                node = q.popleft() # node = 1; 3; null
                if node: # true, true, false
                    rightSide = node # rightSide = 1; 3
                    q.append(node.left) # q = [2], q = [null, 2]
                    q.append(node.right) # q = [3, 2], q = [null, null, 2]

            if rightSide: # true
                res.append(rightSide.val) # res = [1, 3]

        return res
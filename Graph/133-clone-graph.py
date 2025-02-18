'''
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {} # hashset to track nodes

        def dfs(node):
            # If node is already cloned, return its copy
            if node in oldToNew:       
                return oldToNew[node]   

            # Create a new node (clone) with the same value as the original node
            copy = Node(node.val)
            # Store the mapping of original node to cloned node       
            oldToNew[node] = copy

            # Recursively clone all neighbours and add them to the cloned node's neighbors list       
            for nei in node.neighbors:  
                copy.neighbors.append(dfs(nei))
                # Return the cloned node
            return copy
        
        # If the input node is not None, start the DFS cloning process
        return dfs(node) if node else None
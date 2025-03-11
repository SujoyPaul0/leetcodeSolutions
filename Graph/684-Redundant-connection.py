'''
Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
'''

from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Initialize parent array where each node is its own parent
        par = [i for i in range(len(edges) + 1)]
        # Initialize rank array to keep track of tree depth
        rank = [1] * (len(edges) + 1)

        # Find function with path compression
        def find(n):
            p = par[n]
            # Traverse up to find the root parent
            while p != par[p]:
                par[p] = par[par[p]]  # Path compression: Make node point directly to its grandparent
                p = par[p]
            return p

        # Union function with union by rank
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)  # Find the root parents of both nodes

            if p1 == p2:
                return False  # Cycle detected if both nodes have the same root

            # Merge the smaller tree into the larger tree to keep tree balanced
            if rank[p1] > rank[p2]:
                par[p2] = p1  # Attach p2's tree to p1
                rank[p1] += rank[p2]  # Update rank of p1
            else:
                par[p1] = p2  # Attach p1's tree to p2
                rank[p2] += rank[p1]  # Update rank of p2
            return True  # Union successful

        # Process each edge
        for n1, n2 in edges:
            if not union(n1, n2):  # If union fails, a cycle is found
                return [n1, n2]  # Return the redundant edge

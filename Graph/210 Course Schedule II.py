from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Create an adjacency list (prereq) to store the prerequisites for each course.
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # Step 2: Initialize structures to track the result (output), visited nodes, and cycles.
        output = []  # Stores the topological ordering of courses
        visit = set()  # Tracks courses that have been fully processed (added to output)
        cycle = set()  # Tracks courses in the current recursion stack to detect cycles

        # Step 3: Depth-First Search (DFS) function to traverse the graph
        def dfs(crs):
            # If a cycle is detected (course is already in the current recursion stack), return False
            if crs in cycle:
                return False
            # If the course has already been visited and added to output, no need to process again
            if crs in visit:
                return True

            # Mark the course as part of the current cycle
            cycle.add(crs)
            # Recur for all prerequisites (dependencies) of the current course
            for pre in prereq[crs]:
                if dfs(pre) == False:  # If a cycle is found in the recursion, return False
                    return False
            # After all prerequisites are processed, remove the course from the cycle set
            cycle.remove(crs)
            # Mark the course as fully processed
            visit.add(crs)
            # Add the course to the output list (since it has no unprocessed prerequisites)
            output.append(crs)
            return True  # Course processing successful

        # Step 4: Perform DFS for each course to determine the order
        for c in range(numCourses):
            if dfs(c) == False:  # If a cycle is detected in any DFS call, return an empty list
                return []

        # Step 5: Return the valid course ordering (reverse order of output since DFS adds courses after dependencies)
        return output

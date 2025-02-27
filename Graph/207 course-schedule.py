'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Create a HashMap to store prerequisite relationships
        # Each course points to a list of courses that must be completed before it
        preMap = { i:[] for i in range(numCourses)}

        # Step 2: Populate the prerequisite map
        # Example: If prerequisites = [[1,0]], it means "To take course 1, you must complete course 0 first
        for crs, pre in prerequisites: 
            preMap[crs].append(pre)

        # Step 3: Create a set to track courses currently in the DFS path
        # This helps detect cycles in the prerequisite graph
        visitSet = set()

        # Step 4: Define a DFS function to check if a course can be completed
        def dfs(crs):
            # If the course is already in the visitSet, we have a cycle -> return False
            if crs in visitSet:
                return False

            # if the course has no prerequisites, it can be completed -> return  True
            if preMap[ crs ] == []:
                return True

            # Add the current course to the visitSet to track the DFS path
            visitSet.add(crs)

            # Step 5: Recursively check ilf all prerequisites for this course can be completed
            for pre in preMap[crs]:
                if not dfs(pre): # If any prereqyisite can't be completed , return False
                    return False 
            
            # Step 6: If all prerequisites are met, remove the course from visitSet
            visitSet.remove(crs)

            # mark the course as "can be completed" by clearing its prerequisite list
            preMap[crs] = []
            return True

        # Step 7: Run DFS on all courses
        for crs in range(numCourses):
            if not dfs(crs): # If any course can't be completed, return False
                return False

        # If DFS completes for all courses without detecting a cycle, return True
        return True

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        # populate hashmap
        for pre, crs in prerequisites:
            preMap[pre].append(crs)

        visitSet = set()
        # dfs
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True

            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visitSet.remove(crs)
            preMap[crs] = []
            return True

        # result
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
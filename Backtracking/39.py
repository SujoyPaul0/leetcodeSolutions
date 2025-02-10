'''
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # depth first search recursion, i-index, cur-current value arrays
        def dfs(i, cur, total):
            # it total = target append a copy of cur
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            # decision to include ith element
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            # decision not to include
            # clear cur
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
'''
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort the candidates to efficiently avoid duplicates
        candidates.sort()

        res = []
        # backtracking
        def backtrack(cur, pos, target):
            # if target becomes 0 after decrementin
            if target == 0:
                res.append(cur.copy())
            # if target becomes -ve
            if target <= 0:
                return
            # keep track of previous to avoid
            prev = -1
            # iterate from cur pos to len
            for i in range(pos, len(candidates)):
                # if candidates[i] and prev is same then continue loop
                if candidates[i] == prev:
                    continue
                # append ith candidate
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return res

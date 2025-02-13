'''
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set() 
        posDiag = set() # determined by (r + c)
        negDiag = set() # determined by (r - c)

        res = [] # all possible sols
        board = [["."] * n for i in range(n)] # create board with . in it

        def backtrack(r):
            # if we ever reach n th row that means we found a solution
            if r == n:
                # create a copy of board as string as mentioned in ques
                copy =["".join(row) for row in board] 
                res.append(copy)
                return

            # iterate for range of n
            for c in range(n):
                # check if c or (r + c) or (r - c) already have been used
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                # update sets
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                # update board
                board[r][c] = "Q"

                # backtrack to next row
                backtrack(r + 1)

                # cleanup for backtrack
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                # clean board
                board[r][c] = "."

        backtrack(0)
        return res
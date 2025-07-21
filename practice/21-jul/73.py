class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows= [] 
        cols = []
        rowCnt, colCnt = len(matrix), len(matrix[0])

        for r in range(rowCnt):
            for c in range(colCnt):
                if matrix[r][c] == 0:
                    rows.append(r)
                    cols.append(c)

        for r in rows:
            for i in  range(colCnt):
                matrix[r][i] = 0
        
        for c in cols:
            for i in  range(rowCnt):
                matrix[i][c] = 0
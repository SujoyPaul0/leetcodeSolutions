class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]

        matrix = [[0] * n for _ in range(n)]

        l, r = 0, n
        top, bot = 0, n
        ele = 0

        while l < r and top < bot:
            for i in range(l, r):
                ele += 1
                matrix[top][i] = ele
            top += 1

            for i in range(top, bot):
                ele += 1
                matrix[i][r-1] = ele
            r -= 1

            if not (l < r and top < bot):
                break

            for i in range(r-1, l-1, -1):
                ele += 1
                matrix[bot - 1][i] = ele
            bot -= 1

            for i in range(bot -1, top -1, -1):
                ele += 1
                matrix[i][l] = ele
            l += 1
            
        return matrix
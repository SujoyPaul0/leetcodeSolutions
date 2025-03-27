'''
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
    
        while l < r:
            for i in range(r-l):
                top = l
                bottom = r
                
                # store top-left element in var
                var = matrix[top][l + i]

                # store bottom-left in top-right
                matrix[top][l + i] = matrix[bottom - i][l]

                # store top-left in bottom-right
                matrix[bottom - i][l] = matrix[bottom - i][r]

                # store top right in bottom right
                matrix[bottom - i][r] = matrix[top + i] [r]

                # store var in top-left
                matrix[top + i][r] = var

            l += 1
            r -= 1   
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        first_row_got_zero = False
        first_col_got_zero = False

        for m in range(row):
            for n in range(col):
                if matrix[m][n] == 0:
                    if m == 0:
                        first_row_got_zero = True
                    if n == 0:
                        first_col_got_zero = True
                    matrix[0][n] = matrix[m][0] = 0

        for i in range(1,row):
            for j in range(1,col):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
                else:
                    matrix[i][j]

        if first_col_got_zero:
            for i in range(row):
                matrix[i][0] = 0
        
        if first_row_got_zero:
            for j in range(col):
                matrix[0][j] = 0




        
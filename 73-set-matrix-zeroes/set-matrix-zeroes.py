class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        flag_row = [False] * row
        flag_col = [False] * col
        for m in range(row):
            for n in range(col):
                if matrix[m][n] == 0:
                    flag_row[m] = True
                    flag_col[n] = True
        for i in range(len(flag_row)):
            for j in range(len(flag_col)):
                if flag_row[i] == True or flag_col[j] == True:
                    matrix[i][j] = 0


        
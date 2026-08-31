class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        zero_first_row = False
        zero_first_col = False

        for j in range(0, len(matrix[0])):
            if matrix[0][j] == 0:
                zero_first_row = True
        
        for i in range(0, len(matrix)):
            if matrix[i][0] == 0:
                zero_first_col = True

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        for j in range(0, len(matrix[0])):
            if zero_first_row:
                matrix[0][j] = 0
        
        for i in range(0, len(matrix)):
            if zero_first_col:
                matrix[i][0] = 0


        
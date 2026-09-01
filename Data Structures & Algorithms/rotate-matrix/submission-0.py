class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        # transpose
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # flip over y axis
        for i in range(len(matrix)):
            for j in range(len(matrix[0])//2):
                matrix[i][j], matrix[i][len(matrix)-j-1] = matrix[i][len(matrix)-j-1], matrix[i][j]
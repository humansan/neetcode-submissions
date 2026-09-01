class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        nums_count = len(matrix) * len(matrix[0])
        left, right, top, bottom = 0, 0, 0, 0

        spiral_out = []

        while len(spiral_out) < nums_count:

            # top row -> left to right
            i = left
            while len(spiral_out) < nums_count and i < len(matrix[0])-right:
                spiral_out.append(matrix[top][i])
                i += 1
            top += 1

            # print(spiral_out)

            # right column -> top to bottom 
            i = top
            while len(spiral_out) < nums_count and i < len(matrix)-bottom:
                spiral_out.append(matrix[i][len(matrix[0])-right-1])
                i += 1
            right += 1

            # print(spiral_out)

            # bottom row -> right to left
            i = len(matrix[0]) - right - 1
            while len(spiral_out) < nums_count and i >= left:
                spiral_out.append(matrix[len(matrix) - bottom - 1][i])
                i -= 1
            bottom += 1

            # print(spiral_out)

            # left column -> bottom to top
            i = len(matrix) - bottom - 1
            while len(spiral_out) < nums_count and i >= top:
                spiral_out.append(matrix[i][left])
                i -= 1
            left += 1

            # print(spiral_out)

            

        return spiral_out


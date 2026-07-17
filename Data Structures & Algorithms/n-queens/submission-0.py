class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        rows = [False] * n
        cols = [False] * n
        up_right = [False] * (2*n-1) # x + y is the same -> x+y is the index
        down_right = [False] * (2*n-1) # x - y is the same -> x-y + n-1 is the index

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(x):

            if(x == n):
                res.append(["".join(q) for q in board])
            
            for y in range(n):
                if cols[y]:
                    continue
                if up_right[x+y]:
                    continue
                if down_right[x - y + n-1]:
                    continue
                
                board[x][y] = "Q"
                cols[y] = True
                up_right[x+y] = True
                down_right[x - y + n-1] = True
                backtrack(x+1)
                board[x][y] = "."
                cols[y] = False
                up_right[x+y] = False
                down_right[x - y + n-1] = False
        
        backtrack(0)
        return res

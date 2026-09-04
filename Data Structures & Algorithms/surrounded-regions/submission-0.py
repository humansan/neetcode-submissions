class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS = len(board)
        COLS = len(board[0])
        
        def run_bfs(x, y):

            if 0 <= x < ROWS and 0 <= y < COLS and board[x][y] == 'O':

                board[x][y] = 'Y' # serves 2 purposes, marks it as part of a edge bordering region, and also acts as a visited state so it isn't revisited

                run_bfs(x + 1, y)
                run_bfs(x - 1, y)
                run_bfs(x, y + 1)
                run_bfs(x, y - 1)

        for i in range(ROWS):
            for j in range(COLS):
                # run bfs from the edge cells
                if i == 0 or i == (ROWS-1) or j == 0 or j == (COLS-1):
                    run_bfs(i, j)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'Y':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # create bfs
        # to prevent loops or visiting already set cells, instead of tracking visited, put a condition where we only go to the next cell if the number of current cell is lower (or less than value - 1 even)
        # run bfs from water cells

        ROWS = len(grid)
        COLS = len(grid[0])

        INF = 2147483647

        q = deque()

        # add to queue all the treasure chests
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j))

        # while loop needs to expand outwards from chests, and in each iteration mark reached cells with distance. increase distance after each iteration
        distance = 0
        while q:
            cur_cells = len(q)

            for i in range(cur_cells):
                r, c = q.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] > distance + 1:
                        grid[nr][nc] = distance + 1
                        q.append((nr, nc))

            distance += 1

        # loop through grid, and if cell is 0, run bfs

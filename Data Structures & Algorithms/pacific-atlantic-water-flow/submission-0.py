class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        set_atlantic, set_pacific = set(), set()
        nrows, ncols = len(heights), len(heights[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        q = deque()

        queue_atlantic = deque()
        queue_pacific = deque()

        for ROW in range(nrows):
            queue_atlantic.append((ROW, ncols-1))
            set_atlantic.add((ROW, ncols-1))

            queue_pacific.append((ROW, 0))
            set_pacific.add((ROW, 0))

        for COL in range(ncols):
            queue_atlantic.append((nrows-1, COL))
            set_atlantic.add((nrows-1, COL))

            queue_pacific.append((0, COL))
            set_pacific.add((0, COL))

        def bfs(q, set_):
            while q:
                x, y = q.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < nrows and 0 <= ny < ncols and (nx,ny) not in set_ and heights[nx][ny] >= heights[x][y]:
                        q.append((nx,ny))
                        set_.add((nx,ny))

        bfs(queue_atlantic, set_atlantic)
        bfs(queue_pacific, set_pacific)

        return list(set_atlantic & set_pacific)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()

        fresh_oranges = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh_oranges += 1

        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q and fresh_oranges > 0:
            minutes += 1
            length_this_minute = len(q)
            print(minutes, q)
            for i in range(length_this_minute):
                cur_x, cur_y = q.popleft()

                for dr, dc in directions:
                    x = dr + cur_x
                    y = dc + cur_y

                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh_oranges -= 1

                        q.append((x, y))
                    
        if fresh_oranges == 0:
            return minutes
        return -1
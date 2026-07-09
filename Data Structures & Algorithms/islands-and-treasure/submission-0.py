class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        INF = 2147483647
        
        # need to do multi source BFS. Go outward from the treasures instead

        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()

            for x, y in directions:
                dr, dc = x + r, y + c

                if (
                    dr in range(rows) and
                    dc in range(cols) and
                    grid[dr][dc] == INF
                ): 
                    grid[dr][dc] = grid[r][c] + 1
                    queue.append((dr, dc))





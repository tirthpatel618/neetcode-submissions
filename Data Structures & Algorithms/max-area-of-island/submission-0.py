class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 

        rows = len(grid)
        cols = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visited = set()
        max_area = 0

        def bfs(row, col):
            visited.add((row, col))
            queue = deque()
            queue.append((row, col))
            area = 1

            while queue: 
                row, col = queue.popleft()
                for x, y in directions: 
                    dr = row + x
                    dc = col + y
                    if (dr in range(rows)) and (dc in range(cols)) and (grid[dr][dc] == 1) and ((dr, dc) not in visited):
                        queue.append((dr, dc))
                        visited.add((dr, dc))
                        area += 1
            return area


        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = bfs(r, c)
                    print(area)
                    max_area = max(area, max_area)
        return max_area
        
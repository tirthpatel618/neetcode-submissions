class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def bfs(row, col):
            visited.add((row, col))
            queue = deque()
            queue.append((row, col))

            while queue:
                r, c = queue.popleft()
                # add its neighbours to the queue
                #has to be in range, has to be a 1, has to be not visited
                for dr, dc in directions:
                    xr = r + dr
                    xc = c + dc
                    if ((xr in range(rows)) and (xc in range(cols))
                        and grid[xr][xc] == "1" and ((xr, xc) not in visited)):
                        queue.append((xr, xc))
                        visited.add((xr, xc))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
        return islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()

        ROWS = len(grid)
        COLS = len(grid[0])

        islands = 0

        def dfs(row, col):
            if (
                row < 0 or col < 0 or
                row >= ROWS or col >= COLS or
                grid[row][col] == "0" or
                (row, col) in visited
            ):
                return

            visited.add((row, col))

            for x, y in dirs:
                dr = row + x
                dc = col + y
                dfs(dr, dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1

        return islands
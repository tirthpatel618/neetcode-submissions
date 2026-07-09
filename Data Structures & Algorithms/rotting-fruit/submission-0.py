class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        BFS. work outward from the rotten fruit. At minute 0 put all of them in a queue. 
        queue should have the rotten ones in a list, so that we know how to track minutes

        make a set of all the fresh fruit, remove from it as we rot

        """
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROTTEN = 2
        FRESH = 1

        queue = deque()
        fresh_fruits = set()

        level = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == ROTTEN:
                    level.append((r, c))
                if grid[r][c] == FRESH:
                    fresh_fruits.add((r, c))
        
        queue.append(level)
        minute = 0

        while queue:
            curr_level = queue.popleft()
            new_level = []

            for r, c in curr_level:
                for x, y in directions: 
                    dr, dc = r + x, c + y
                    if (dr in range(rows)) and (dc in range(cols)) and grid[dr][dc] == FRESH:
                        grid[dr][dc] = ROTTEN
                        fresh_fruits.remove((dr, dc))
                        new_level.append((dr, dc))
            if new_level:
                queue.append(new_level)
                minute += 1
            

        return minute if not fresh_fruits else -1



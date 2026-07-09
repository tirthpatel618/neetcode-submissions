class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Solution 
        Running dfs on every cell would be too much cost. you run it mn times which runs for mn time each
        instead, to keep it just mn, run it only on border. Work inwards. 
        Instead of one source to 2 destinations, flip it to 2 sources to many destinations

        flood from pacific edges inwards. then from atlantic ones. take the intersection
        """
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        def dfs(r, c, visit, prevHeight):
            if (
                (r, c) in visit or
                r < 0 or c < 0 or
                r == rows or c == cols or 
                heights[r][c] < prevHeight
            ):
                return 
            visit.add((r,c))
            for x, y in directions:
                dr, dc = r + x, c + y
                dfs(dr, dc, visit, heights[r][c])
        
        #traverse the sea. mark visitable sets for both
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows -1, c, atl, heights[rows - 1][c])
        
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        
        res = list(pac & atl)
        return res
        



        
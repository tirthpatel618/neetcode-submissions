class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        # visit all that can possibly be visited from this node
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        
        def bfs(start):
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                
        
        res = 0
        # singular nodes are components too. 
        # find a component each call to dfs. 
        for node in range(n):
            if node not in visited:
                visited.add(node)
                bfs(node)
                res += 1
        return res

        #DO BFS TOO FOR THIS
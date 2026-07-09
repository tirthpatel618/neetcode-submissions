class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree if it is connected and has no cycles. 
        # BUT n-1 edges + connected implies no cycles
        # only with edge set

        # first construct graph from edgeset. 
        # need a valid u,v path for all u, v in edges -> too much work
        # best way to check connected? must have n-1 edges

        if len(edges) != n-1:
            return False

        visited = set()
        #build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            # RMR - duplicates not shown. so have to add to both since its undirected
            graph[u].append(v)
            graph[v].append(u)

        # start dfs on a node, once it finishes, the # of nodes it visits should be n
        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                dfs(neighbor, node)
        
        dfs(0, -1)
        
        return True if len(visited) == n else False



    
        

        
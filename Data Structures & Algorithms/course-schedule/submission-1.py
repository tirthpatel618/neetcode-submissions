class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        For directed graphs, think in 3 states. unvisited, visiting, finished
        This is cycle detection. If there is any cycle in pre reqs, it cant be done
        """
        # build an adjacency list, where each prereq is mapped to its courses
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        #cycle comes if while on your visiting path, 
        # you have a neighbour in the visiting state

        state = [0] * numCourses

        def dfs(node):
            if state[node] == VISITING:
                return False
            if graph[node] == []:
                return True
            
            state[node] = VISITING

            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False
            state[node] = VISITED
            graph[node] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            


        
        

            



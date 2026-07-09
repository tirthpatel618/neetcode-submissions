class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        output = []
        visited, path = set(), set()

        def dfs(course):
            if course in path: 
                return False
            if course in visited:
                return True
            
            path.add(course)
            for neighbour in graph[course]:
                if not dfs(neighbour):
                    return False
            
            path.remove(course)
            visited.add(course)
            output.append(course)
            return True

        for c in range(numCourses):
            if c not in visited:
                if dfs(c) == False:
                    return []
        return output
        
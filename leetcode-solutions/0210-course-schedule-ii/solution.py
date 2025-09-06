class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        visited = set()
        path = set()
        graph = defaultdict(list)

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        
        def dfs(i):
            path.add(i)
            visited.add(i)

            for neighbors in graph[i]:
                if neighbors not in visited:
                    if not dfs(neighbors):
                        return False
                
                elif neighbors in visited and neighbors in path:
                    # found false case
                    return False

                # if escaped
            path.remove(i)
            res.append(i)
            return True

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []
        
        return res
                    

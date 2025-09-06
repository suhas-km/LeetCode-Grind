class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph from given edges
        # create a new visited set = pathVisited, visited
        # traverse that graph and use visited set, if you find a circle/ return true if this escapes false

        graph = defaultdict(list)

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        
        pathVisited = set() # path of the current dfs - will be reset
        visited = set() # all nodes in the 

        def dfs(i):
            # initially add to set
            pathVisited.add(i)
            visited.add(i)
            
            for neighbors in graph[i]:
                if neighbors not in visited:
                    if not dfs(neighbors):
                        return False

                elif neighbors in visited and neighbors in pathVisited:
                    # found false case
                    return False
                # if escaped
            pathVisited.remove(i)

            return True

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i): 
                    return False
        
        return True

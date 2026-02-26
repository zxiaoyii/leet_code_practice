from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # model the directed graph
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        # bfs
        queue = deque(i for i in range(numCourses) if indegree[i] == 0)
        res = []

        while queue:
            node = queue.popleft()
            res.append(node)
            for course in graph[node]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        return res if len(res) == numCourses else []
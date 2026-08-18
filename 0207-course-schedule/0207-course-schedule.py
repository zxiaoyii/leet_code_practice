class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # model the graph
        # course -> [list of course can be taken after took this course]
        graph = defaultdict(list) 
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # dijkstra
        queue = deque([i for i in range(len(indegree)) if indegree[i] == 0])

        while queue:
            idx = queue.popleft()
            for course in graph[idx]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)

        for i in indegree:
            if i != 0:
                return False
        return True
        
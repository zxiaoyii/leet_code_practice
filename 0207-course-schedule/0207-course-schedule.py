class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        #model graph
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        queue = deque([i for i in range(len(indegree)) if indegree[i] == 0])

        while queue:
            c = queue.popleft()
            for course in graph[c]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        for i in indegree:
            if i != 0:
                return False
        return True



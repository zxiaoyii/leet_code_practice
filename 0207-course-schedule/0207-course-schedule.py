from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list) #course -> []
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        count = 0 # how may course finished
        while queue:
            course = queue.popleft()
            count += 1
            for next_c in graph[course]:
                indegree[next_c] -= 1
                if indegree[next_c] == 0:
                    queue.append(next_c)
        return count == numCourses



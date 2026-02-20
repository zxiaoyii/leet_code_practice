from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # put prereq into a directed graph
        graph = defaultdict(list) # b -> [a1, a2, ...]
        indegree = [0] * numCourses #record how may nodes pointed to one node
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        res = []
        while queue:
            c = queue.popleft()
            res.append(c)
            for a in graph[c]:
                indegree[a] -= 1
                if indegree[a] == 0:
                    queue.append(a)
        
        return res if len(res) == numCourses else []



        

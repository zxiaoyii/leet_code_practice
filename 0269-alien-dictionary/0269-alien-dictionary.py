class Solution:
    def alienOrder(self, words: List[str]) -> str:
        #adjacency list
        graph = {c : set() for word in words for c in word}

        #get word order
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break

        #calculate indegree   
        indegree = {c: 0 for c in graph}
        for c in graph:
            for neighbor in graph[c]:
                indegree[neighbor] += 1
        #bfs/ kahn's algorithm
        queue = deque([c for c in indegree if indegree[c] == 0])
        res = []

        while queue:
            c = queue.popleft()
            res.append(c)
            for neighbor in graph[c]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(res) != len(graph):
            return ""
        
        return "".join(res)

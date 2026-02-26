class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # model graph
        graph = defaultdict(set)
        indegree = {c: 0 for word in words for c in word}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            #非法
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
            
        queue = deque(c for c in indegree if indegree[c] == 0)
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for course in graph[node]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        if len(res) != len(indegree):
            return ""
        return "".join(res)
        

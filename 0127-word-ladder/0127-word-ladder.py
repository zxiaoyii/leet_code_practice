class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        # bfs
        queue = deque([(1, beginWord)])
        visited = set()
        visited.add(beginWord)
        while queue:
            step, word = queue.popleft()
            for i in range(len(word)):
                for c in ascii_lowercase:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word == endWord:
                        return step + 1
                    if new_word in wordSet and new_word not in visited:
                        visited.add(new_word)
                        queue.append((step + 1, new_word))
        return 0
                        
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordList:
            return 0
        
        queue = deque([(1, beginWord)])
        visited = {beginWord}
        while queue:
            step, word = queue.popleft()
            for i in range(len(word)):
                for c in ascii_lowercase:
                    newWord = word[:i] + c + word[i+1:]
                    if newWord == endWord:
                        return step + 1
                    if newWord in wordSet and newWord not in visited:
                        visited.add(newWord)
                        queue.append((step + 1, newWord))
        return 0
        
                
                
                

from collections import deque
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)

        while queue:
            s, cnt = queue.popleft()
            for i in range(len(s)):
                for c in string.ascii_lowercase:
                    new_word = s[:i] + c + s[i+1:]
                    if new_word == endWord:
                        return cnt + 1
                    if new_word in wordSet and new_word not in visited:
                        queue.append((new_word, cnt + 1))
                        visited.add(new_word)
        return 0

            
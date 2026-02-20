from collections import deque
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        front = {beginWord}
        back = {endWord}
        visited = {beginWord, endWord}
        length = 1
        while front and back:
            length += 1
            #每次选择较小的方向拓展
            if len(front) > len(back):
                front, back = back, front
            #拓展front
            next_front = set()
            for word in front:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        new_w = word[:i] + c + word[i+1:]
                        if new_w in back:
                            return length
                        if new_w in wordSet and new_w not in visited:
                            next_front.add(new_w)
                            visited.add(new_w)
            front = next_front
        return 0

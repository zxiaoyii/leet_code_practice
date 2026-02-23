import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if not endWord in wordSet:
            return 0
        
        
        front = {beginWord}
        back = {endWord}
        visited = {beginWord, endWord}
        res = 1
        
        while front and back:
            res += 1
            if len(front) > len(back):
                front, back = back, front
            next_front = set()
            for word in front:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in back:
                            return res
                        if new_word in wordSet and new_word not in visited:
                            next_front.add(new_word)
                            visited.add(new_word)
            front = next_front
        
        return 0
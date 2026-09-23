class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        return self._dfs(word, 0, self.root)

    def _dfs(self, word: str, i: int, node: TrieNode) -> bool:
        if i == len(word):
            return node.is_end
        c = word[i]
        if c == '.':
            for a, n in node.children.items():
                if self._dfs(word, i + 1, n):
                    return True
            return False
        else:
            if c in node.children:
                return self._dfs(word, i + 1, node.children[c])
            else:
                return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
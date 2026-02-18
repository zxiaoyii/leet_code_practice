class TrieNode:
    def __init__(self):
        self.children = {} #char -> node
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c] 
        node.is_end = True

    def search(self, word: str) -> bool:
        return self._dfs(word, 0, self.root)
 
    def _dfs(self, word: str, i: int, node: TrieNode) -> bool:
        # 递归终止：已处理完所有字符
        if i == len(word):
            return node.is_end

        ch = word[i]

        if ch == '.':
            # 通配符：尝试当前节点的所有子节点
            for child in node.children.values():
                if self._dfs(word, i + 1, child):
                    return True
            return False
        else:
            # 普通字符：正常匹配
            if ch not in node.children:
                return False
            return self._dfs(word, i + 1, node.children[ch])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
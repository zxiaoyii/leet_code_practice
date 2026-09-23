class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            
        node.is_word = True

    def exist(self, word: str) -> TrieNode:
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return None
        return node 


    def search(self, word: str) -> bool:
        node = self.exist(word)
        return node.is_word if node else False
        
    def startsWith(self, prefix: str) -> bool:
        node = self.exist(prefix)
        return True if node else False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
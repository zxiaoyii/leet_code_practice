class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if not c in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True
   
    def search(self, word: str) -> bool:
        a = self._exist(word)
        if a:
            return a
        return False 
        

    def startsWith(self, prefix: str) -> bool:
        return self._exist(prefix) is not None
    
    def _exist(self, w: str) -> bool:
        node = self.root
        for c in w:
            if c in node.children:
                node = node.children[c]
            else:
                return None
        return node.is_end
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
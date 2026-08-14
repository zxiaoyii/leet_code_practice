class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
        
class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        m, n = len(board), len(board[0])
        #put all the words into the Trie
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word
        
        #dfs search from 4 dir of each cell
        dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        def dfs(r, c, node):
            if node.word:
                res.append(node.word)
                node.word = None
            if 0 <= r < m and 0 <= c < n and board[r][c] != "#":    
                ch = board[r][c] #a
                if ch in node.children:
                    board[r][c] = "#"
                    for a, b in dir:
                        dfs(r + a, c + b, node.children[ch])
                    board[r][c] = ch
            return
        
        #iterate through all the cells in the grid and do the dfs
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        
        return res
                
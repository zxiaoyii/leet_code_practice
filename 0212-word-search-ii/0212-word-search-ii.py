class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None #直接存单词，省去回溯拼接

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        
        for s in words:
            node = root
            for c in s:
                if not c in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = s

        rows, cols = len(board), len(board[0])   
        res = []

        def dfs(r, c, node):
            ch = board[r][c]

            if ch not in node.children:
                return
            
            dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            next_node = node.children[ch]

            if next_node.word:
                res.append(next_node.word)
                next_node.word = None
            
            board[r][c] = "#"

            for a, b in dir:
                a1, b1 = r + a, c + b
                if 0 <= a1 < rows and 0 <= b1 < cols and board[a1][b1] != "#":
                    dfs(a1, b1, next_node)

            board[r][c] = ch
            if not next_node.children:
                del node.children[ch]
            
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return res
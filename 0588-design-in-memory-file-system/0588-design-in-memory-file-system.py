class TrieNode:
    def __init__(self):
        self.children = {}
        self.content = ""

class FileSystem:

    def __init__(self):
        self.root = TrieNode() 

    def traverse(self, path):
        """ traverse through the path to the end 
            if path don't exsist, create the path """
        node = self.root
        if path == '/':
            return node
        for part in path.split('/')[1:]:
            if part not in node.children:
                node.children[part] = TrieNode()
            node = node.children[part]
        return node
        

    def ls(self, path: str) -> List[str]:
        node = self.traverse(path)
        # if is file return filename
        if node.content:
            return [path.split('/')[-1]]
        return sorted(node.children.keys())
        
    def mkdir(self, path: str) -> None:
        self.traverse(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.traverse(filePath)
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.traverse(filePath).content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.content = ''

class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        cur = self.mkdir(path)
        if cur.content:
            return [path.split('/')[-1]]
        return sorted(cur.children.keys())
  

    def mkdir(self, path: str) -> None:
        cur = self.root
        if len(path) == 1:
            return cur
        for p in path.split('/')[1:]:
            if p not in cur.children:
                cur.children[p] = TrieNode()
            cur = cur.children[p]
        return cur
    
    
        
    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.mkdir(filePath)
        cur.content += content

    def readContentFromFile(self, filePath: str) -> str:
        cur = self.mkdir(filePath)
        return cur.content

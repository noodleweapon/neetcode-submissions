class TreeNode:
    def __init__(self):
        self.dirs = {}
        self.files = {}
    
    def mkdir(self, segments):
        tree = self
        for segment in segments:
            if segment not in tree.dirs:
                tree.dirs[segment] = TreeNode()
            tree = tree.dirs[segment]
    
    def cd(self, segments):
        tree = self
        for segment in segments:
            tree = tree.dirs[segment]
        return tree
    
    def ls(self, segments):
        tree = self
        n = len(segments)
        for i, segment in enumerate(segments):
            if i == n - 1 and segment in tree.files:
                return [segment]
            tree = tree.dirs[segment]
        res = [*list(tree.dirs.keys()), *list(tree.files.keys())]
        res.sort()
        return res

class FileSystem:

    def __init__(self):
        self.root = TreeNode()
        
    def ls(self, path: str) -> List[str]:
        segments = path.split("/")[1:] if path != "/" else []
        return self.root.ls(segments)

    def mkdir(self, path: str) -> None:
        if path == "/":
            return # already exists
        segments = path.split("/")[1:]
        self.root.mkdir(segments)

    def addContentToFile(self, filePath: str, content: str) -> None:
        segments = filePath.split("/")[1:]
        fileName = segments.pop()
        _dir = self.root.cd(segments)
        if fileName in _dir.files:
            _dir.files[fileName] += content
        else:
            _dir.files[fileName] = content

    def readContentFromFile(self, filePath: str) -> str:
        segments = filePath.split("/")[1:]
        fileName = segments.pop()
        _dir = self.root.cd(segments)
        return _dir.files[fileName]
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)

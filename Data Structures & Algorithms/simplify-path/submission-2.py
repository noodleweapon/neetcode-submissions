class Solution:
    def simplifyPath(self, path: str) -> str:
        elems = path.split('/')
        s = []
        for elem in elems:
            if elem in ['', '.']:
                continue
            if elem == '..':
                if s:
                    s.pop()
                continue
            s.append(elem)
        
        return '/' + '/'.join(s)        

        # /neetcode/practice//...///../courses"
        # /neetcode/practice/courses
        # Input: path = "/../"
        # Output: "/"
        # Input: path = "/_home/a"
        # Output: "/_home/a"
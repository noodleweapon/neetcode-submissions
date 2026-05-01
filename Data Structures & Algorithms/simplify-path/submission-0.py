class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        segs = path.split('/')
        for i, seg in enumerate(segs):
            if seg == '.' or seg == '':
                continue
            if seg == '..':
                if s:
                    s.pop()
                continue
            s.append(seg)
        
        return "/" + "/".join(s)

        # ..
        # /..//_home/a/b/..///
        # .. _home a b ..
        # /_home/a
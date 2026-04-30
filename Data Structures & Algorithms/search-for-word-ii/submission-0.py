class Trie:
    def __init__(self):
        self.d = {}
        self.w = None
    
    def insert(self, word):
        t = self
        for c in word:
            if c not in t.d:
                t.d[c] = Trie()
            t = t.d[c]
        t.w = word
    
    # def find(self, word):
    #     t = self
    #     for c in word:
    #         if c not in t.d:
    #             return None
    #         t = t.d[c]
    #     t.word = None
    #     return t.word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R = len(board)
        C = len(board[0])
        root = Trie()

        for word in words:
            root.insert(word)
        
        found = []
        seen = set()

        def dfs(t, r, c):
            if t.w != None:
                found.append(t.w)
            t.w = None
            
            for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc
                if nc < 0 or nr < 0 or nc >= C or nr >= R:
                    continue
                key = (nr, nc)
                if key in seen:
                    continue
                char = board[r][c]
                if char not in t.d:
                    continue

                seen.add(key)
                dfs(t.d[char], nr, nc)
                seen.remove(key)


        for r in range(R):
            for c in range(C):
                dfs(root, r, c)

        return found
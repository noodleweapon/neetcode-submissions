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
            
            seen.add((r, c))
            for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc
                if nc < 0 or nr < 0 or nc >= C or nr >= R:
                    continue
                if (nr, nc) in seen:
                    continue
                char = board[nr][nc]
                if char not in t.d:
                    continue
                dfs(t.d[char], nr, nc)
            seen.remove((r, c))

        for r in range(R):
            for c in range(C):
                char = board[r][c]
                if char not in root.d:
                    continue
                dfs(root.d[char], r, c)

        return found
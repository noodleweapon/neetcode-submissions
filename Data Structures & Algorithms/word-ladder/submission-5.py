class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
                # ✓ CRITICAL: endWord must be in wordList
        if endWord not in wordList:
            return 0
        
        if beginWord == endWord:
            return 1  # Also: return 1 if they're the same, not 0
        
        n = len(beginWord)
        def can_traverse(w1, w2):
            diff = 0
            for j in range(n):
                if w1[j] != w2[j]:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1
        
        visited = [False] * len(wordList)
        to_visit = deque([beginWord])
        d = 0
        while to_visit:
            d += 1
            for _ in range(len(to_visit)):
                word = to_visit.popleft()
                if can_traverse(word, endWord):
                    return 1 + d
                for i, next_word in enumerate(wordList):
                    if can_traverse(word, next_word):
                        if not visited[i]:
                            visited[i] = True
                            to_visit.append(next_word)
        return 0
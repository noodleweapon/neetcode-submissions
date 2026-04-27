class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        L = len(beginWord)
        def similar(w1, w2):
            mismatches = 0
            for i in range(L):
                if w1[i] != w2[i]:
                    mismatches += 1
                    if mismatches > 1:
                        return False
            return True
            
        N = len(wordList)
        d = 1
        seen = [False] * N
        Q = deque()

        def add(i):
            if seen[i]:
                return
            Q.append(wordList[i])
            seen[i] = True

        for i, word in enumerate(wordList):
            if similar(word, beginWord):
                add(i)

        while Q:
            l = len(Q)
            d += 1
            for _ in range(l):
                w = Q.popleft()
                if w == endWord:
                    return d

                for i, word in enumerate(wordList):
                    if similar(word, w):
                        add(i)

        return 0
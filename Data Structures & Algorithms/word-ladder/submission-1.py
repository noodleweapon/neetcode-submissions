class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        L = len(beginWord)
        N = len(wordList)
        words = set(wordList)
        Q = deque([(beginWord, 1)])

        while Q:
            (word, dist) = Q.popleft()
            if word == endWord:
                return dist
            for i in range(L):
                for c in ALPHABET:
                    nxt = word[:i] + c + word[i+1:]
                    if nxt in words:
                        Q.append((nxt, dist + 1))
                        words.remove(nxt)
        return 0
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        if beginWord == endWord:
            return 1
        n = len(beginWord)
        d = 0
        q = deque([beginWord])
        while q:
            d += 1
            for _ in range(len(q)):
                cur_word = q.popleft()
                for j in range(n):
                    for c in string.ascii_lowercase:
                        if c == cur_word[j]:
                            continue
                        cur_word2 = cur_word[:j] + c + cur_word[j+1:]
                        if cur_word2 == endWord:
                            return d + 1
                        if cur_word2 in words:
                            words.remove(cur_word2)
                            q.append(cur_word2)
        return 0

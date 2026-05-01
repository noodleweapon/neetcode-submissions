class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {c: i for i, c in enumerate(order)}
        n = len(words)
        if n == 1:
            return True

        def is_sorted(w1, w2):
            for i in range(min(len(w1), len(w2))):
                o1 = rank[w1[i]]
                o2 = rank[w2[i]]
                if o1 < o2:
                    return True
                if o1 > o2:
                    return False
            return len(w1) <= len(w2)

        for i in range(n - 1):
            w1, w2 = words[i], words[i + 1]
            if not is_sorted(w1, w2):
                return False
        return True
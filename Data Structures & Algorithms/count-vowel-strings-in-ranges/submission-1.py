class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        V = set('aeiou')
        n = len(words)
        prefix = [0]
        for i in range(n):
            W = words[i]
            add = 1 if (W[0] in V and W[-1] in V) else 0
            prefix.append(prefix[-1] + add)
        return [prefix[r + 1] - prefix[l] for l, r in queries]
        
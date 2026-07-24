class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        byLen = defaultdict(set)
        for word in words:
            byLen[len(word)].add(word)
        lengths = list(sorted(byLen.keys()))
        
        def isConc(word):
            falses = set()
            def rec(i):
                if i == len(word):
                    return True
                if i in falses:
                    return False
                for length in lengths:
                    if length == len(word):
                        continue
                    j = i + length
                    if j > len(word):
                        break
                    if word[i:j] not in byLen[length]:
                        continue
                    if rec(j):
                        return True
                falses.add(i)
                return False
            return rec(0)

        return list(filter(isConc, words))
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        byLen = defaultdict(set)
        for word in words:
            byLen[len(word)].add(word)
        lengths = list(sorted(byLen.keys()))
        
        def isConc(word):
            falses = set()
            def rec(i, count):
                if (i, count > 1) in falses:
                    return False
                if i == len(word):
                    return count > 1
                for length in lengths:
                    j = i + length
                    if j > len(word):
                        break
                    if word[i:j] not in byLen[length]:
                        continue
                    if rec(j, count + 1):
                        return True
                falses.add((i, count > 1))
                return False
            return rec(0, 0)

        return list(filter(isConc, words))
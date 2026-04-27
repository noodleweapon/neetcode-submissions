class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        out = []
        def rec(i, items, rem):
            if rem < 0:
                return
            if i == len(candidates):
                if rem == 0:
                    out.append(items.copy())
                return
            candidate = candidates[i]
            j = i
            while j < len(candidates) and candidate == candidates[j]:
                j += 1
            
            rec(j, items, rem)
            for _ in range(i, j):
                items.append(candidate)
                rem -= candidate
                rec(j, items, rem)

            for _ in range(i, j):
                items.pop()

        rec(0, [], target)
        return out

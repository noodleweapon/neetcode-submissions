class Solution:
    def rec(self, i, cur, res, candidates, target):
        if target == 0:
            res.append(cur.copy())
            return
        if target < 0:
            return
        if i >= len(candidates):
            return

        cur.append(candidates[i])
        self.rec(i + 1, cur, res, candidates, target - candidates[i])
        cur.pop()
        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1
        self.rec(i + 1, cur, res, candidates, target)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        cur, res = [], []
        self.rec(0, cur, res, candidates, target)
        return res
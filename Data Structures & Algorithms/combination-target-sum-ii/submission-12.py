class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        def rec(i, arr, s, skipped):
            if s > target:
                return
            if i == len(candidates):
                if s == target:
                    res.append(arr.copy())
                return

            # skip
            rec(i + 1, arr, s, True)

            # prevent taking after skipping.
            if skipped and candidates[i] == candidates[i - 1]:
                return

            # take
            arr.append(candidates[i])
            rec(i + 1, arr, s + candidates[i], False)
            arr.pop()

        rec(0, [], 0, False)
        return res

        # 1,2,2,2,2,4,6



class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def dfs(i, path, cur):
            if cur == target:
                res.append(path.copy())
                return
            if i == len(candidates) or cur > target:
                return

            # take it
            path.append(candidates[i])
            dfs(i + 1, path, cur + candidates[i])
            path.pop()

            # skip duplicates ONLY if not take.
            j = i + 1
            while j < len(candidates) and candidates[i] == candidates[j]:
                j += 1

            # skip it (and all duplicates)
            dfs(j, path, cur)

        dfs(0, [], 0)
        return res
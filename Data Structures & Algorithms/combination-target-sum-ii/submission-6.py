class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res = []
        def rec(i, items, rem):
            if i == n:
                if rem == 0:
                    res.append(items.copy())
                return

            items.append(candidates[i])
            rec(i + 1, items, rem - candidates[i])
            items.pop()
            for j in range(i + 1, n):
                if candidates[j] != candidates[i]:
                    rec(j, items, rem)
                    return
            rec(i + 1, items, rem)

        rec(0, [], target)
        return res


        # 55555555

        # 9,2,2,4,6,1,5
        # 1,2,2,4,5,6,9



        # [1,2,3,4,5]

        # [1,2,4],
        # [2,5],
        # [3,4]
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
            
            if rem < 0:
                return

            items.append(candidates[i])
            rec(i + 1, items, rem - candidates[i])
            items.pop()

            j = i + 1
            while j < n and candidates[j] == candidates[i]:
                j += 1
            rec(j, items, rem)

        rec(0, [], target)
        return res


        # 55555555

        # 9,2,2,4,6,1,5
        # 1,2,2,4,5,6,9



        # [1,2,3,4,5]

        # [1,2,4],
        # [2,5],
        # [3,4]
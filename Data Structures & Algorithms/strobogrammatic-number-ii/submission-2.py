class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        PAIRS = [('6', '9'), ('9', '6'), ('1', '1'), ('8', '8'), ('0', '0')]
        SINGLES = ['0', '1', '8']

        res = []

        def rec(l, r, L, R):
            if l == r + 1: # base case
                arr = L + list(reversed(R))
                res.append("".join(arr))
            elif l < r:
                for lpair, rpair in PAIRS:
                    if l == 0 and lpair == '0':
                        continue
                    L.append(lpair)
                    R.append(rpair)
                    rec(l + 1, r - 1, L, R)
                    L.pop()
                    R.pop()
            elif l == r:
                for num in SINGLES:
                    L.append(num)
                    rec(l + 1, r, L, R)
                    L.pop()
        
        rec(0, n - 1, [], [])
        return res

        # 6969 √
        # 609 √
        # 690 x
        # 0 -- this
        # 1 -- this
        # 8 -- this
        # 6, 9
        # 2 and 5 ?
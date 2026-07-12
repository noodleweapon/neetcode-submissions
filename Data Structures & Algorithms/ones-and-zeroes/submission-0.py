class Solution:
    def findMaxForm(self, strs: List[str], zeros: int, ones: int) -> int:
        dp = [[0] * (zeros + 1) for _ in range(ones + 1)]
        # dp[a][b] is how many arr we can fit with a zeros and b ones.
        for s in strs:
            c = Counter(list(s))
            cost_ones = c['1']
            cost_zeros = c['0']
            for _ones in reversed(range(cost_ones, ones + 1)):
                for _zeros in reversed(range(cost_zeros, zeros + 1)):
                    dp[_ones][_zeros] = max([
                        dp[_ones][_zeros],
                        dp[_ones - cost_ones][_zeros - cost_zeros] + 1
                    ])
        return dp[ones][zeros]




        # Misunderstood problem:
        # res = 0
        # for s in strs:
        #     zeros = Counter(list(s))['0']
        #     ones = Counter(list(s))['1']
        #     if zeros <= m and ones <= n:
        #         res += 1
        # return res
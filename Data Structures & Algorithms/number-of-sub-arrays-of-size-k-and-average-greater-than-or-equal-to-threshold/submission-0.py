class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s = 0
        l = 0
        n = 0
        for r in range(len(arr)):
            s += arr[r]
            if r - l >= k:
                s -= arr[l]
                l += 1
            size = (r - l + 1)
            if size != k:
                continue

            if s >= threshold * size:
                n += 1
        return n
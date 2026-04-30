class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        ts = []
        for k, v in d.items():
            ts.append(tuple(k, v))
        
        ts.sort(key=lambda t: t[1])
        return ts[:k]
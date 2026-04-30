class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        ts = []
        for k, v in d.items():
            ts.append((k, v))
        
        ts.sort(key=lambda t: t[1], reverse=True)
        vs = list(map(lambda t : t[0], ts[:k-1]))
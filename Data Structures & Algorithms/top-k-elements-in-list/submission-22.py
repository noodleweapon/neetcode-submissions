class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        elems = [(v, key) for key, v in c.items()]
        heapq.heapify(elems)
        return list(map(lambda x: x[1], heapq.nlargest(k, elems)))
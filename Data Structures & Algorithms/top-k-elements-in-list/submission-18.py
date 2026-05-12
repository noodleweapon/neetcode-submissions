class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return list(map(lambda x: x[0], count.most_common(k)))

        # d = defaultdict(int)
        # for num in nums:
        #     d[num] += 1
        
        # heap = []
        # for kk in d.keys():
        #     tup = (d[kk], kk)
        #     heapq.heappush(heap, tup)
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # return list(map(lambda t : t[1], heap))


        # ts = []
        # for kk, v in d.items():
        #     ts.append((kk, v))
        
        # ts.sort(key=lambda t: t[1], reverse=True)
        # vs = list(map(lambda t : t[0], ts[:k]))
        # return vs


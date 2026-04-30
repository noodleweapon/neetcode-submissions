class Twitter:

    def __init__(self):
        self.f = defaultdict(set)
        self.p = defaultdict(list)
        self.c = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.p[userId].append((-self.c, tweetId))
        self.c += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for post in self.p[userId]:
            heapq.heappush(heap, post)
        for uid in self.f[userId]:
            for post in self.p[uid]:
                heapq.heappush(heap, post)
        res = heapq.nsmallest(10, heap)
        print(res)
        return list(map(lambda x : x[1], res))

    def follow(self, followerId: int, followeeId: int) -> None:
        self.f[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.f[followerId].discard(followeeId)

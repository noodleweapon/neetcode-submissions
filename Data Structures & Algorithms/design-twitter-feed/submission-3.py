class Twitter:

    def __init__(self):
        self.t = 0
        self.posts = {}
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.t += 1
        if userId not in self.posts:
            self.posts[userId] = deque()
        self.posts[userId].append((-self.t, tweetId))
        if len(self.posts[userId]) > 10:
            self.posts[userId].popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        for channelId in list(self.following[userId]) + [userId]:
            if channelId not in self.posts:
                continue
            for post in self.posts[channelId]:
                heapq.heappush(h, post)
        return list(map(lambda x: x[1], heapq.nsmallest(10, h)))

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].remove(followeeId)

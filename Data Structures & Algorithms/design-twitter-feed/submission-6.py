class Twitter:

    def __init__(self):
        self.t = 0
        self.posts = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.t += 1
        self.posts[userId].append((-self.t, tweetId))
        if len(self.posts[userId]) > 10:
            self.posts[userId].pop(0)

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        channelIds = self.following[userId] | {userId}
        for channelId in channelIds:
            l = len(self.posts[channelId])
            if l == 0:
                continue
            (t, tweetId) = self.posts[channelId][l - 1]
            heapq.heappush(h, (t, tweetId, channelId, l - 1))
        
        res = []
        while h and len(res) < 10:
            (t, tweetId, channelId, ind) = heapq.heappop(h)
            res.append(tweetId)
            if ind > 0:
                (nt, newTweetId) = self.posts[channelId][ind - 1]
                heapq.heappush(h, (nt, newTweetId, channelId, ind - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

class Twitter:
    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        users = self.follows[userId] | {userId}
        for user in users:
            if self.tweets[user]:
                idx = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][idx]
                heapq.heappush(heap, (time, tweetId, user, idx - 1))

        while heap and len(res) < 10:
            time, tweetId, user, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx >= 0:
                ntime, ntweetId = self.tweets[user][idx]
                heapq.heappush(heap, (ntime, ntweetId, user, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
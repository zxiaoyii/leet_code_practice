class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list) #userId -> [(time, tweetId), ...]
        self.following = defaultdict(set) #userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.following[userId] | {userId}
        for uid in users:
            if self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                t, tid = self.tweets[uid][idx]
                heapq.heappush(heap, (-t, tid, uid, idx))
        res = []
        while heap and len(res) < 10:
            neg_t, tid, uid, idx = heapq.heappop(heap)
            res.append(tid)
            if idx > 0:
                idx -= 1
                t, tid = self.tweets[uid][idx]
                heapq.heappush(heap, (-t, tid, uid, idx))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
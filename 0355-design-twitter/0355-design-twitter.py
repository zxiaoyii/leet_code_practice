class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []
        people = self.following[userId] | {userId}
        for uid in people:
            lst = self.tweets[uid]
            if lst:
                i = len(lst) - 1
                t, tid = lst[i]
                heapq.heappush(heap, (-t, tid, uid, i))
        
        res = []
        while heap and len(res) < 10:
            negT, tid, uid, i = heapq.heappop(heap)
            res.append(tid)
            if i > 0:
                t2, tid2 = self.tweets[uid][i - 1]
                heapq.heappush(heap, (-t2, tid2, uid, i - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
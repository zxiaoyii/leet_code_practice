class Twitter:

    def __init__(self):
        self.following = defaultdict(set) # {followerId: {followeeId, ..}}
        self.tweets = defaultdict(list) # {userId: [(time, tweetId), ..]}
        self.time = 0 # tweet  time += 1
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # add foloweeId + userId into one list
        users = list(self.following[userId]) + [userId]
        users = self.following[userId] | {userId}
        
        # pq = []
        # for user in users:
        #     for time, tweet in self.tweets[user][-10:]:
        #         heapq.heappush(pq, (time, tweet))
        #         if len(pq) > 10:
        #             heapq.heappop(pq)
          #O(10*nlog10)          
        # res = []
        # while pq:
        #     _, tweet = heapq.heappop(pq)
        #     res.append(tweet)
        #O(10log10)
        # return res[::-1]

        heap = []
        for user in users:
            if self.tweets[user]:
                idx = len(self.tweets[user]) - 1
                time, t_id = self.tweets[user][idx]
                heapq.heappush(heap, (-time, t_id, user, idx))
        #O(nlogn)
        res = []
        while heap and len(res) < 10:
            t, t_id, user, idx = heapq.heappop(heap)
            res.append(t_id)
            if idx > 0:
                idx -= 1
                time, tweetId = self.tweets[user][idx]
                heapq.heappush(heap, (-time, tweetId, user, idx))
        return res
        #O(10logn)  
        #500
                 

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
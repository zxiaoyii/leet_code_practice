class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        count = Counter(hand) # get the num of each cards
        keys = sorted(count) # sort from small to big
        for k in keys:
            if count[k] > 0:
                n = count[k]
                for i in range(groupSize):
                    count[k + i] -= n
                    if count[k + i] < 0:
                        return False
        return True



        
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # return Counter(nums).most_common(1)[0][0]
        count = 0
        candidate = None
        for x in nums:
            if count == 0:
                candidate = x
            count += 1 if x == candidate else -1
        return candidate
        
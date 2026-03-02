class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        sum = 0
        res = 0
        for num in nums:
            sum += num
            if sum - k in prefix:
                res += prefix[sum - k]
            prefix[sum] += 1
        return res
class Solution:
    def rob(self, nums: list[int]) -> int:
        #dp[n + 2] = max(dp[n] + num[n + 2], dp[n + 1])
        a = 0
        b = 0
        res = 0
        for num in nums:
            res = max(a + num, b)
            a = b
            b = res
        return res
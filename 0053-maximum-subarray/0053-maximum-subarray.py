class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = nums[0]
        res = nums[0]
        i = 1
        while i < len(nums):
            a = nums[i]
            cur = max(a, cur + a)
            res = max(res, cur)
            i += 1
        return res

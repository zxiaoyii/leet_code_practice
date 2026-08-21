class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = 0
        res = 0
        for n in nums:
            prev = max(n, prev + n)
            res = max(res, prev)
        return res

        

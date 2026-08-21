class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = nums[0]
        res = nums[0]
        for n in nums[1:]:
            prev = max(n, prev + n)
            res = max(res, prev)
        return res

        

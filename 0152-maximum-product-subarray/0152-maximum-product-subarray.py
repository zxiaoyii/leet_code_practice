class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = cur_max = cur_min = nums[0]
        for num in nums[1:]:
            cands = (num, cur_max * num, cur_min * num)
            cur_max, cur_min = max(cands), min(cands)
            res = max(res, cur_max)
        return res
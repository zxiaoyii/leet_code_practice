class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        new_nums = set(nums)
        res = 0
        for n in new_nums:
            if n - 1 in new_nums:
                continue
            l = 1
            while n + 1 in new_nums:
                l += 1
                n += 1
            res = max(res, l)
        return res
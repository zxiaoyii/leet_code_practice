class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i, val in Counter(nums).items():
            if val == 1:
                return i
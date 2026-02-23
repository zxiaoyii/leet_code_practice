class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        a = nums[0]
        nums.remove(a)
        nums.sort()
        return nums[0] + nums[1] + a
        
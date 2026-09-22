class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = []
        temp = 1
        for n in nums:
            res.append(temp)
            temp *= n
        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= temp
            temp *= nums[i]
        return res
            
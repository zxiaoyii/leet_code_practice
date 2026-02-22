class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        far = 0
        curEnd = 0
        
        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])
            if i == curEnd:
                steps += 1
                curEnd = far
        return steps
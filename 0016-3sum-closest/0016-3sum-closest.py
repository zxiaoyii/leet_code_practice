class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() 
        res = float('inf')
        # [-1, -1, 0, 1, 2, 3]
        for i in range(len(nums) - 2): 
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:    
                val_r = nums[r]
                val_l = nums[l]
                sum = val_r + val_l + nums[i]
                if sum == target:
                    return target
                elif sum > target:
                        r -= 1
                elif sum < target:
                        l += 1
                if abs(res - target) > abs(sum - target):
                    res = sum
                        
        return res
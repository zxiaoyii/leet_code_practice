class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        # [-1, -1, 0, 1, 2, 3]
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                val_r = nums[r]
                val_l = nums[l]
                sum = val_r + val_l + nums[i]
                if sum == 0:
                    res.append([val_r, val_l, nums[i]])
                    while l < r and val_l == nums[l + 1]:
                        l += 1
                    while l < r and val_r == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif sum > 0:
                        r -= 1
                elif sum < 0:
                        l += 1
        return res
                    
                    
            
            
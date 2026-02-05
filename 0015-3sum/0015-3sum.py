class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       #[a, b, c] -> b + c = -a = k
        res = []
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            a = nums[i]
            if a > 0:
                continue
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                b = nums[l]
                c = nums[r]
                sum = b + c
                if sum == -a:
                    res.append([a, b, c])
                    while l < r and nums[l + 1] == b:
                        l += 1
                    while l < r and nums[r - 1] == c:
                        r -= 1
                    l += 1
                    r -= 1
                elif sum < -a:
                    l += 1 
                else:
                    r -=1
        return res
            
                    
            
                
       
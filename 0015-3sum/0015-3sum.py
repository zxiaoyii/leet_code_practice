class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        l = len(nums)
        res = []
        for i, a in enumerate(nums):
            if a > 0:
                return res
            if i > 0 and a == nums[i - 1]:
                continue
            target = -a
            j = i + 1
            k = l - 1
            while j < k:
                b = nums[j]
                c = nums[k]
                if c < 0:
                    break
                total = b + c
                if total > target:
                    k -= 1
                elif total < target:
                    j += 1
                else:
                    res.append([a, b, c])
                    while k > j and nums[k - 1] == c:
                        k -= 1
                    while k > j and nums[j + 1] == b:
                        j += 1
                    k -= 1
                    j += 1 
        return res
            
                

            
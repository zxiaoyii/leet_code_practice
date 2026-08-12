class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            a = nums[l]
            b = nums[mid]
            c = nums[r]
            if b > c:
                l = mid + 1
            elif b < a:
                r = mid
            else:
                return nums[l]
        return nums[l]
                

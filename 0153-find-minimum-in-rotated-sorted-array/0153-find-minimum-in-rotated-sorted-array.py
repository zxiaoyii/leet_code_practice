class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0 
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1        # 断崖在右边,最小值在 mid 之后
            else:
                r = mid            # 断崖在左边(或没断崖),最小值在 mid 及之前
        return nums[l]

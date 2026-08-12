class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # 判断左半部分是否有序
            if nums[l] <= nums[mid]:
                # 左半部分有序，检查 target 是否在左半部分范围内
                if nums[l] <= target < nums[mid]:
                    r = mid - 1   # 在左半部分
                else:
                    l = mid + 1    # 在右半部分
            else:
                # 右半部分有序，检查 target 是否在右半部分范围内
                if nums[mid] < target <= nums[r]:
                    l = mid + 1    # 在右半部分
                else:
                    r = mid - 1   # 在左半部分
        
        return -1  # 未找到

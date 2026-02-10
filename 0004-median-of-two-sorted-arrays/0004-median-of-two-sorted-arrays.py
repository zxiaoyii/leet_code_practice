class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2
        l, r = 0, m
        while l <= r:
            i = l + (r - l) // 2
            j = half - i
            nums1_left = nums1[i - 1] if i > 0 else float('-inf')
            nums1_right = nums1[i] if i < m else float('inf')
            nums2_left = nums2[j - 1] if j > 0 else float('-inf')
            nums2_right = nums2[j] if j < n else float('inf')
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (m + n) % 2 == 1:
                    return max(nums1_left, nums2_left)  # 奇数：左半边最大值
                else:
                    return (max(nums1_left, nums2_left) +
                            min(nums1_right, nums2_right)) / 2  # 偶数：取平均
            elif nums1_left > nums2_right:
                r = i - 1  # nums1 取多了，往左收
            else:
                l = i + 1   # nums1 取少了，往右扩

        return 0  # 不会到这里
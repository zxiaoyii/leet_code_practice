class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        half_length = (m + n + 1) // 2
        l, r = 0, m

        while l <= r:
            i = (l + r) // 2
            j = half_length - i
            nums1_a = nums1[i - 1] if i > 0 else float('-inf')
            nums1_b = nums1[i] if i < m else float('inf')
            nums2_a = nums2[j - 1] if j > 0 else float('-inf')
            nums2_b = nums2[j] if j < n else float('inf')
            if nums1_a <= nums2_b and nums1_b >= nums2_a:
                if (m + n) % 2 == 1:
                    return float(max(nums1_a, nums2_a))
                else:
                    return (max(nums1_a, nums2_a) + min(nums1_b, nums2_b)) / 2
            elif nums1_a > nums2_b:
                r = i - 1 
            else:
                l = i + 1
                 


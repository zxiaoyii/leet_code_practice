class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        length = (m + n + 1) // 2
        l, r = 0, m
        while l <= r:
            i = (l + r) //2
            j = length - i
            a = nums1[i - 1] if i > 0 else float('-inf')
            b = nums1[i] if i < m else float('inf')
            c = nums2[j - 1] if j > 0 else float('-inf')
            d = nums2[j] if j < n else float('inf')
            if a > d:
                r = i - 1
            elif b < c:
                l = i + 1
            elif a <= d and b >= c:
                if (m + n) % 2 == 1:
                    return float(max(a, c))
                else:
                    return (max(a, c) + min(b, d)) / 2

        
        
        

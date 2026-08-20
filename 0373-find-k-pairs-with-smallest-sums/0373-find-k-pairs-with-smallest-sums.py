class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # 堆中存 (和, i, j)
        heap = []
        # 初始：nums1 每个元素都和 nums2[0] 配对
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        
        res = []
        while heap and len(res) < k:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            
            # 只有 nums2 指针向后移动
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        
        return res
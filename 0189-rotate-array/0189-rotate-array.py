class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # 处理 k > n 的情况
        result = [0] * n
        
        for i in range(n):
            result[(i + k) % n] = nums[i]
        
        # 复制回原数组
        for i in range(n):
            nums[i] = result[i]
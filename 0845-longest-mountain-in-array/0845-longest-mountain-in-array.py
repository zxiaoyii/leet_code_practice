class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        
        max_length = 0
        i = 1
        
        while i < n - 1:
            # 检查是否是山脚（开始上山的点）
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                # 找到山顶，向左右扩展
                left = i - 1
                while left > 0 and arr[left-1] < arr[left]:
                    left -= 1
                
                right = i + 1
                while right < n - 1 and arr[right] > arr[right+1]:
                    right += 1
                
                # 计算山脉长度
                length = right - left + 1
                max_length = max(max_length, length)
                
                # 直接从山脉右侧继续查找
                i = right
            else:
                i += 1
        
        return max_length

        
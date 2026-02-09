class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = []  # 单调递增栈，存储索引
        max_area = 0
        
        for i in range(len(heights)):
            # 当前高度小于栈顶高度时，开始计算面积
            while stack and heights[stack[-1]] > heights[i]:
                # 弹出栈顶索引
                h_index = stack.pop()
                h = heights[h_index]  # 高度
                
                # 计算宽度
                # 左边界是新的栈顶，右边界是当前位置 i
                w = i - stack[-1] - 1
                
                # 计算面积并更新最大值
                max_area = max(max_area, h * w)
            
            # 当前索引入栈
            stack.append(i)
        
        return max_area
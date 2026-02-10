class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # storing the index
        max_area = 0
        heights = [0] + heights + [0]
        
        for i in range(len(heights)):
            #[1, 5, 6] <- 2
            while stack and heights[stack[-1]] > heights[i]:
                h_index = stack.pop() # index of 6 #[1, 5] <- 2
                h = heights[h_index] # 6
                w = i - stack[-1] - 1 # 1
                #index of 2 - index of 5 - 1  = 5 - 3 - 1 = 1
                area = h * w
                max_area = max(max_area, area)
            stack.append(i)
        return max_area
            
                
                
                
                
                
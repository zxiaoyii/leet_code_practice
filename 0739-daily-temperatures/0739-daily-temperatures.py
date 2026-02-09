class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n      # 初始化全0
        stack = []            # 单调栈，存索引
        
        for i in range(n):
            # 当前温度 > 栈顶温度，找到答案了
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            
            stack.append(i)   # 当前索引入栈
        
        return answer

            
            
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # 栈底放一个-1，作为参考点
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                # 左括号入栈
                stack.append(i)
            else:
                # 右括号，弹出栈顶
                stack.pop()
                
                if not stack:
                    # 栈空了，说明当前右括号没有匹配的左括号
                    # 将当前索引作为新的参考点
                    stack.append(i)
                else:
                    # 计算当前有效括号长度
                    max_len = max(max_len, i - stack[-1])
        
        return max_len
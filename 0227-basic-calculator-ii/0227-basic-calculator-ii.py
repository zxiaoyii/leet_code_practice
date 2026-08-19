class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'  # 当前数字前面的符号，初始为 '+'
        
        for i, char in enumerate(s):
            # 如果是数字，构建完整的数字
            if char.isdigit():
                num = num * 10 + int(char)
            
            # 如果是运算符，或者是最后一个字符
            if char in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    # 注意：Python 的 // 对负数会向下取整，需要用 int() 截断
                    stack.append(int(stack.pop() / num))
                
                # 更新符号和数字
                sign = char
                num = 0
        
        # 栈中所有元素相加
        return sum(stack)

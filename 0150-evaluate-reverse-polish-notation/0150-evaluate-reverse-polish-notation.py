class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        s1 = []
        for s in tokens:
            if s not in ('+', '-', '*', '/'):
                s1.append(int(s))
            else:
                b = s1.pop()
                a = s1.pop()
                if s == '+':
                    res = a + b
                elif s == '-':
                    res = a - b
                elif s == '*':
                    res = a * b
                elif s == '/':
                    res = int(a / b)
                s1.append(res)
        return s1[0]

            
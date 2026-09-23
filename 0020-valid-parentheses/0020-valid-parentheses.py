class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")":"(", "]":"[", "}":"{"}
        stack = []
        for c in s:
            if c not in dic:
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack.pop() != dic[c]:
                    return False
        return not stack

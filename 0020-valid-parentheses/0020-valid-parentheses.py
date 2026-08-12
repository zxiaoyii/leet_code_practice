class Solution:
    def isValid(self, s: str) -> bool:
        mp = {"}":"{", "]":"[", ")":"("}
        stack = []
        for c in s:
            if c in mp:
                if not stack:
                    return False
                c1 = stack.pop()
                if c1 != mp[c]:
                    return False
            else:
                stack.append(c)
        return True if len(stack) == 0 else False
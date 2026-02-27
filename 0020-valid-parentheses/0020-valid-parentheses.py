class Solution:
    def isValid(self, s: str) -> bool:
        mp = {")": "(", "}": "{", "]" : "["}

        stack = []
        for c in s:
            if c in mp.keys():
                if not stack:
                    return False
                new_c = stack.pop()
                if mp[c] != new_c:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
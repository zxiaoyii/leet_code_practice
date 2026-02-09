class Solution:
    def isValid(self, s: str) -> bool:
        mp = {')':'(', ']':'[', '}':'{'}
        stack = []
        for c in s:
            if stack and c in mp:
                if mp[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        return False if stack else True
                

                
        
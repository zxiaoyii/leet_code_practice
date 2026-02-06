class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        need = Counter(t)
        window = {}
        l = 0
        valid = 0
        start = 0
        length = float('inf')
        for r in range(len(s)):
            c = s[r]
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need):
                if r - l + 1 < length:
                    start = l
                    length = r - l + 1
                d = s[l]
                l += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return "" if length == float('inf') else s[start: start + length]

        
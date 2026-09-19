class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n, m = len(s), len(p)
        if n < m:
            return []
        
        need = Counter(p)
        window = Counter(s[:m])
        res = [0] if window == need else []

        for i in range(m, n):
            window[s[i]] += 1
            window[s[i - m]] -= 1
            if window[s[i - m]] == 0:
                del window[s[i - m]]
            if window == need:
                res.append(i - m + 1)
        return res





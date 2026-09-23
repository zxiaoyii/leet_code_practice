class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        l = 0
        res = 0
        maxf = 0
        for r, c in enumerate(s):
            window[c] += 1
            maxf = max(maxf, window[c])
            if r - l + 1 - maxf > k:
                window[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


            
            
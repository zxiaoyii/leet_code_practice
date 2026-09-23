class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        l = 0
        res = 0
        for r, c in enumerate(s):
            while c in window and l <= r:
                del window[s[l]]
                l += 1
            window[c] = 1
            res = max(res, r - l + 1)

        return res



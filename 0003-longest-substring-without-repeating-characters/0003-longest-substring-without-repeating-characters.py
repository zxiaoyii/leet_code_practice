class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        res = 0
        for r, c in enumerate(s):
            while c in window and l <= r:
                window.remove(s[l])
                l += 1
            window.add(c)
            res = max(res, r - l + 1)

        return res



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = defaultdict(int)
        res = 0
        for r in range(len(s)):
            ch = s[r]
            if ch in seen and seen[ch] >= l:
                l = seen[ch] + 1
            seen[ch] = r
            res = max(res, r - l + 1)
        return res


   
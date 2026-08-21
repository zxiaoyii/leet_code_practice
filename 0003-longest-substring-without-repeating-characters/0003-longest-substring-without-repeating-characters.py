class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) == 0:
        #     return 0
        l = 0
        window = defaultdict(int)
        res = 0
        for r in range(len(s)):
            ch = s[r]
            window[ch] += 1
            while window[ch] > 1:
                chl = s[l]
                window[chl] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
        
    
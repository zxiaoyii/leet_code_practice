class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        if len(s) <= k:
            return len(s)
        
        l = 0
        window = defaultdict(int) # ch -> count
        res = 0
        for r in range(len(s)):
            ch = s[r]
            window[ch] += 1
            while len(window) > k:
                temp = s[l]
                window[temp] -= 1
                if window[temp] == 0:
                    del window[temp]
                l += 1
            if len(window) <= k:
                res = max(res, r - l + 1)
        return res
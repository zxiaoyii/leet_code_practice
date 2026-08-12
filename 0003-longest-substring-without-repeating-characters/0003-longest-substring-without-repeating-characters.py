class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        d = defaultdict(int) 
        for right in range(len(s)):
            c = s[right] 
            d[c] += 1
            while d[c] > 1:
                d[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
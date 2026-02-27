class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        res = 0
        left = 0
        cnt = defaultdict(int)
        for right in range(len(s)):
            cnt[s[right]] += 1
            while cnt[s[right]] > 1:
                cnt[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
            
                
            

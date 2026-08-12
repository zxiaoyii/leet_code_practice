class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_c = 0
        d = defaultdict(int)
        for right in range(len(s)):
            d[s[right]] += 1
            max_c = max(max_c, d[s[right]])
            if right - left + 1 - max_c > k:
                d[s[left]] -= 1
                left += 1
        return len(s) - left
                 
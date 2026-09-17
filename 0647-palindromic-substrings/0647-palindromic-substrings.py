class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        def expand(i, j):
            cnt = 0
            while i >= 0 and j < n and s[i] == s[j]:
                cnt += 1
                i -= 1
                j += 1
            return cnt

        for i in range(n):
            res += expand(i, i)      # 奇数长度，单字符为中心
            res += expand(i, i + 1)  # 偶数长度，两字符之间为中心
        return res

       
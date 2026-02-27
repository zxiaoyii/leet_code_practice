class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        n = len(s)
        def expand(i, j):
            if 0 <= i and j < n and s[i] == s[j]:
                return expand(i - 1, j + 1)
            return s[i + 1 : j]

        for i in range(n):
            odd = expand(i, i)
            even = expand(i, i + 1)
            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even
        return res


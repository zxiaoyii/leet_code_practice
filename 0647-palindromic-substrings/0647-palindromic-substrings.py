class Solution:
    def countSubstrings(self, s: str) -> int:
        self.res = 0
        n = len(s)
        def check(i, j):
            if 0 <= i and j < n and s[i] == s[j]:
                self.res += 1
                check(i - 1, j + 1)
            return
        
        for i in range(n):
            a = check(i, i)
            b = check(i, i + 1)

        return self.res
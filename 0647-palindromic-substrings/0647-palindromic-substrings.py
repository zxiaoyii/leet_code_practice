class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        self.res = 0
        def check(i, j):
            if 0 <= i and j < n and s[i] == s[j]:
                self.res += 1
                check(i - 1, j + 1)
            return

        res = 0
        for i in range(n):
            check(i, i)
            check(i, i + 1)
            
        return self.res
            


       
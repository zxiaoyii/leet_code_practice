class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(l, r, path):
            if l == n and r == n:
                res.append(''.join(path))
                return  
            if r < l:
                path.append(')')
                backtracking(l, r + 1, path)
                path.pop()

            if l < n:
                path.append('(')
                backtracking(l + 1, r, path)
                path.pop()
        backtracking(0, 0, [])  
        return res          
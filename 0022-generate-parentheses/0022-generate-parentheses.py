class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path, left, right):
            if left == 0 and right == 0:
                res.append(''.join(path))
                return 
            if left > 0:
                path.append('(')
                backtrack(path, left - 1, right)
                path.pop()
            if right > left:
                path.append(')')
                backtrack(path, left, right - 1)
                path.pop()
        
        backtrack([], n, n)
        return res
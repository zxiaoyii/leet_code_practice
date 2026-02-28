class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []

        def backtracking(idx, path):
            if idx == len(digits):
                res.append("".join(path))
                return

            for c in hashmap[digits[idx]]:
                path.append(c)
                backtracking(idx + 1, path)
                path.pop()

        backtracking(0, [])
        return res
                
                
        
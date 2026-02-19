class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []

        def backtrack(idx, path):
            if idx == len(digits):
                res.append(''.join(path[:]))
                return 
            
            for ch in phone_map[digits[idx]]:
                path.append(ch)
                backtrack(idx + 1, path)
                path.pop()
        
        backtrack(0, [])
        return res


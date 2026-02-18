class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # used = [Fales] * len(nums)
        def backtrack(path, selection):
            if not selection:
                res.append(path[:])
                return 
            for i in range(len(selection)):
                num = selection[i]
                path.append(num)
                selection.pop(i)
                backtrack(path, selection)
                selection.insert(i, num)
                path.pop()
            
        
        backtrack([], nums[:])
        return res          
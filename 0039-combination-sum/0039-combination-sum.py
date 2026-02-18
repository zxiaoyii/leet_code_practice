class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(path, start, sum):
            if sum == target:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target - sum:
                    break
                path.append(candidates[i])
                backtrack(path, i ,sum + candidates[i]) #可重复所以是i
                path.pop()


        candidates.sort()
        backtrack([], 0, 0)
        return res
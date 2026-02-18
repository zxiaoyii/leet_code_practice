class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(path, start):
            res.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                num = nums[i]
                path.append(num)
                backtrack(path, i + 1)
                path.pop()
            
        backtrack([], 0)
        return res
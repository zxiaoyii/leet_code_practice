class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numSet = set(nums)
        length = 0
        for num in numSet:
            if num - 1 in numSet:
                continue
            tempLen = 1
            while num + 1 in numSet:
                tempLen += 1
                num += 1
            length = max(length, tempLen)
        return length

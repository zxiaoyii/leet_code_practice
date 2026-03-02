class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)
        for i, num in enumerate(nums):
            temp = target - num
            if num in hashmap:
                return [hashmap[num], i]
            hashmap[temp] = i
        
            
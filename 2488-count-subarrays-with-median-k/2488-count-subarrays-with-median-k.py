class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        idx = nums.index(k)
        n = len(nums)
        res = 0

        freq = defaultdict(int)
        balance = 0
        for i in range(idx, -1, -1):
            if nums[i] > k:
                balance += 1
            elif nums[i] < k:
                balance -= 1
            freq[balance] += 1
        balance = 0
        for i in range(idx, n):
            if nums[i] > k:
                balance += 1
            elif nums[i] < k:
                balance -= 1
            res += freq[-balance] + freq[1 - balance]
        return res
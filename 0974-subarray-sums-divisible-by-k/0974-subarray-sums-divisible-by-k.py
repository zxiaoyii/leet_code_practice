class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        total = 0
        res = 0

        for n in nums:
            total += n
            left = total % k
            if left == 0:
                res = res + 1 + prefix[0]
            elif left in prefix:
                res += prefix[left]
            prefix[left] += 1
        return res



            
            
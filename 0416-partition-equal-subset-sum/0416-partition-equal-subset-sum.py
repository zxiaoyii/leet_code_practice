class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        # 总和为奇数，不可能平分
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True  # 凑出0总是可行的（什么都不选）
        
        for num in nums:
            # 0/1背包核心：容量从大到小遍历，保证每个数字只用一次
            for j in range(target, num - 1, -1):
                dp[j] = max(dp[j], dp[j - num])
        
        return dp[target]
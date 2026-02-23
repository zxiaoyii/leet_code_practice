class Solution:
    def climbStairs(self, n: int) -> int:
        
        # n stairs
        # step = 1 or 2
        # if num1 + 2 = num2 + 1 = num3
        # num1's step + num2's step = num3's step
        if n == 1:
            return 1

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n - 1]
        
            


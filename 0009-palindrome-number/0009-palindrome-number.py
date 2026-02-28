class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 负数、末尾为0（且不为0本身）直接排除
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # 偶数位：x == reversed_half
        # 奇数位：x == reversed_half // 10（中间位不影响）
        return x == reversed_half or x == reversed_half // 10

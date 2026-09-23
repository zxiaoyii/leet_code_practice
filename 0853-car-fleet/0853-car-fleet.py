class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []
        for p, s in pairs:
            t = (target - p) / s
            if not stack or t > stack[-1]:
                stack.append(t)
        return len(stack)
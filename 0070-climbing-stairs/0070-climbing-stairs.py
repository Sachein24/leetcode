class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n   # IMPORTANT: for climbing stairs, return n, not 1

        a, b = 1, 2  # ways to reach step 1 and step 2

        for _ in range(3, n + 1):
            a, b = b, a + b

        return b

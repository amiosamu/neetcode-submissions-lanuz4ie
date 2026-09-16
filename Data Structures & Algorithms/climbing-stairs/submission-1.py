class Solution:
    def memo(self, n: int, cache: list[int]) -> int:
        if n <= 1:
            return 1

        if cache[n] != -1:
            return cache[n]

        cache[n] = (
            self.memo(n - 1, cache) +
            self.memo(n - 2, cache)
        )
        return cache[n]

    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n + 1)
        return self.memo(n, cache)
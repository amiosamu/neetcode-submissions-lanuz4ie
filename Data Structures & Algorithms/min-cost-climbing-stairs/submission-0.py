class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        n = len(cost)

        def inner(n):
            if n <= 1:
                return 0

            if n in cache:
                return cache[n]
            
            cache[n] = min(inner(n-1) + cost[n-1], inner(n - 2) + cost[n-2])
            return cache[n]

        return inner(n)
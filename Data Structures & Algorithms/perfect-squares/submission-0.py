class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}
        def inner(target):
            if target == 0:
                return 0
            if target in memo:
                return memo[target]
            res = target
            for i in range(1, target):
                if i * i > target:
                    break
                res = min(res, 1 + inner(target - i * i))
            memo[target] = res
            return res
        return inner(n)
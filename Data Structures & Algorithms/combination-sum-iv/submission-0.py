class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(t):
            if t == 0:
                return 1
            if t < 0:
                return 0
            if t in memo:
                return memo[t]
            res = 0
            for num in nums:
                res += dfs(t - num)
            memo[t] = res
            return res
        result = dfs(target)
        print (memo)
        return dfs(target)
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, path = [], []
        def dfs(start: int, remain: int) -> None:
            if remain == 0:
                res.append(path[:])
                return
            for i in range(start, len(nums)):
                if nums[i] > remain:
                    break
                path.append(nums[i])
                dfs(i, remain - nums[i])
                path.pop()
        dfs(0, target)
        return res
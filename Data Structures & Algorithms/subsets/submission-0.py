class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def backtrack(acc, start):
            if start > n:
                return
            result.append(acc[:])
            for i in range(start, n):
                acc.append(nums[i])
                backtrack(acc, i + 1)
                acc.pop()
        backtrack([], 0)
        return result
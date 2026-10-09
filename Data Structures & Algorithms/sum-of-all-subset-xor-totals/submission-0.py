class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def backtrack(i, subset):
            nonlocal res
            count = 0
            for num in subset:
                count ^= num
            res += count

            for j in range(i, len(nums)):
                subset.append(nums[j])
                backtrack(j + 1, subset)
                subset.pop()
        backtrack(0, [])
        return res
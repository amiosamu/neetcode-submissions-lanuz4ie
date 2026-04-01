class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for i, v in enumerate(nums):
            result ^= i ^ v
        return result
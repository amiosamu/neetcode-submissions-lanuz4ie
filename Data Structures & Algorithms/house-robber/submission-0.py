class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def inner(nums):
            n = len(nums)
            if n == 0:
                return 0
            if n == 1:
                return nums[0]
            if n in cache:
                return cache[n]

            cache[n] = max(nums[0] + inner(nums[2:]), inner(nums[1:]))
            return cache[n]
            

        return inner(nums)
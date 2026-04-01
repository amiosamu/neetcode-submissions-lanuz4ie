class Solution:

    def singleNumber(self, nums):
        return reduce(lambda a, b: a ^ b, nums)

    def singleNumber(self, nums):
        result = 0
        for n in nums:
            result ^= n
        return result
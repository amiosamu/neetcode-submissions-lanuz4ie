class Solution:
    def maxSubarraySumCircular(self, nums):
        total = sum(nums)
        maxSum = self.kadaneMax(nums)
        minSum = self.kadaneMin(nums)
        circularSum = total - minSum

        if circularSum == 0:
            return maxSum
        return max(maxSum, circularSum)

    def kadaneMax(self, nums):
        currSum = nums[0]
        globalMax = nums[0]
        for i in range(1, len(nums)):
            currSum = max(nums[i], currSum + nums[i])
            globalMax = max(globalMax, currSum)
        return globalMax

    def kadaneMin(self, nums):
        currSum = nums[0]
        globalMin = nums[0]
        for i in range(1, len(nums)):
            currSum = min(nums[i], currSum + nums[i])
            globalMin = min(globalMin, currSum)
        return globalMin
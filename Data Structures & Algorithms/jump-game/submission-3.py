class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        for i in range(len(nums)-1):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + nums[i])
        return maxReach >= len(nums) - 1
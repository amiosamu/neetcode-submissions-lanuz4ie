class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            left = i + 1
            right = n - 1

            while left < right:
                cur_sum = nums[left] + nums[right]

                if cur_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicate second values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif cur_sum > target:
                    right -= 1
                else:
                    left += 1

        return result
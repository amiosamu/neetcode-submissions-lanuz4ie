class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        curr_sum = 0
        prefixSums = {0:1}
        
        for num in nums:
            curr_sum += num
            if curr_sum - k in prefixSums:
                result += prefixSums[curr_sum - k]
            prefixSums[curr_sum] = prefixSums.get(curr_sum, 0) + 1

        return result
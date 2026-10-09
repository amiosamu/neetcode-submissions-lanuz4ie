class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(acc):
            if len(acc) == len(nums):
                result.append(acc[:])
            for num in nums:
                if num not in acc:
                    acc.append(num)
                    backtrack(acc)
                    acc.pop()


        backtrack([])
        return result
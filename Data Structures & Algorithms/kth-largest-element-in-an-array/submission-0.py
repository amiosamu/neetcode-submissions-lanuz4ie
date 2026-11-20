class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negate = [-num for num in nums]
        heapq.heapify(negate)
        while k != 0:
            res = heapq.heappop(negate)
            k = k - 1
        return -res

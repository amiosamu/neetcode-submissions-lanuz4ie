class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = deque(nums)
        k %= len(nums)

        for _ in range(k):
            d.appendleft(d.pop())
        nums[:] = list(d)
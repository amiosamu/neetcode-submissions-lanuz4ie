class Solution:

        def countOnes(self, n: int) -> int:
            res = 0
            for i in range (0, 31):
                mask = 1 << i
                if (mask & n) != 0:
                    res += 1
            return res

        def countBits(self, n) -> List[int]:
            res = []
            for i in range(0, n+1):
                count = self.countOnes(i)
                res.append(count)
            return res


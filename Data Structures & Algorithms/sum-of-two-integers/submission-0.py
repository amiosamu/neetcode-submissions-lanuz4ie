class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  # 32 ones — keeps arithmetic inside 32 bits
        MAX  = 0x7FFFFFFF  # 2^31 - 1 — boundary between positive and negative

        while b & MASK:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        return a if a <= MAX else ~(a ^ MASK)
class Solution:
    def isHappy(self, n):
        def get_next(self, num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit   # FIXED
                num //= 10
            return total
        
        slow = n
        fast = get_next(self, n)
        
        while fast != 1 and slow != fast:
            slow = get_next(self, slow)
            fast = get_next(self, get_next(self, fast))
        
        return fast == 1

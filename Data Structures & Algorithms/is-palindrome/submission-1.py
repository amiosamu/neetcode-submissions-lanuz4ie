class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = ""
        for c in s:
            if c.isalnum():
                filtered_string += c
        l  = 0
        r = len(filtered_string) - 1
        while l <= r:
            if filtered_string[l].lower() != filtered_string[r].lower():
                return False
            l += 1
            r -= 1
        return True
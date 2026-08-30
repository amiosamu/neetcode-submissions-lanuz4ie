class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = ""
        for c in s:
            if isalnum(c):
                filtered_string += c
        print(filtered_string)
        return True
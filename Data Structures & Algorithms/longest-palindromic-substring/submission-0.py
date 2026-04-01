class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > resLen:
                    res = s[l:r+1]
                    resLen = length
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > resLen:
                    res = s[l:r+1]
                    resLen = length
                l -= 1
                r += 1

        return res

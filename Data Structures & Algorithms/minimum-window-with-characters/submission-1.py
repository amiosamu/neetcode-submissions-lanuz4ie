class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        mappa, window = {}, {}
        for c in t:
            mappa[c] = 1 + mappa.get(c,0)
        have, need = 0, len(mappa)
        res, resLen = [-1,-1], float("inf")
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c,0) + 1
            if c in mappa and window[c] == mappa[c]:
                have += 1

            while have == need:
                if right - left + 1 < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                window[s[left]] -= 1
                if s[left] in mappa and window[s[left]] < mappa[s[left]]:
                    have -= 1
                left += 1
        if resLen == float("inf"):
            return ""
        return s[res[0]:res[1] + 1]

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t is None:
            return ""

        mappa,window = {},{}
        for c in t:
            mappa[c] = 1 + mappa.get(c,0)
        
        have, need = 0, len(mappa)
        res, resLen = [-1,-1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in mappa and window[c] == mappa[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in mappa and window[s[l]] < mappa[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
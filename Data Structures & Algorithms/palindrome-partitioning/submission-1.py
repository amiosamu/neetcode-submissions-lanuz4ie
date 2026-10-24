class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, path = [], []

        def is_pal(lo, hi):
            while lo < hi:
                if s[lo] != s[hi]:
                    return False
                lo += 1
                hi -= 1
            return True
        def dfs(start) -> None:
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start, len(s)):
                if not is_pal(start, end):
                    continue
                path.append(s[start:end + 1])
                dfs(end + 1)
                path.pop()
        dfs(0)
        return res
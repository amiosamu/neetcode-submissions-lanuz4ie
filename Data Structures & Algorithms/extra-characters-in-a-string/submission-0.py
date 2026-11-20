class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = TrieNode()
        for word in dictionary:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = True
        dp = {}
        def dfs(i: int):
            if i == len(s):
                return 0
            if i in dp:
                return dp[i]
            res = 1 + dfs(i + 1)
            curr = root
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.word == True:
                    res = min(dfs(j+1), res)
            dp[i] = res
            return res
        return dfs(0)







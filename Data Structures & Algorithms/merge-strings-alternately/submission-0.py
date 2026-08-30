class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        i, j = 0,0
        out = []
        while i < l1 or j < l2:
            if i < l1:
                out.append(word1[i])
                i += 1
            if j < len(word2):
                out.append(word2[j])
                j += 1
        return "".join(out)
                

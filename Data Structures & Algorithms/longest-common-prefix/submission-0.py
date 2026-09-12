class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for current in strs[1:]:
            j = 0
            while j < len(prefix) and j < len(current):
                if prefix[j] != current[j]:
                    break
                j += 1
            prefix = prefix[:j]
            if prefix == "":
                break
        return prefix
        
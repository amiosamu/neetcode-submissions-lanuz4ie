class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {ch: i for i, ch in enumerate(order)}
        for w1, w2 in zip(words, words[1:]):
            for i in range(len(w1)):
                if i == len(w2):
                    return False
                if w1[i] != w2[i]:
                    if rank[w1[i]] > rank[w2[i]]:
                        return False
                    break

        return True
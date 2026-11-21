class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()
        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = True

        rows = len(board)
        cols = len(board[0])
        res = set()
        visited = set()
        def dfs(r, c, node, word):

            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or board[r][c] not in node.children:
                return
            
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.word == True:
                res.add(word)
            
            visited.add((r,c))
            dfs(r-1,c,node,word)
            dfs(r,c-1,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c+1,node,word)
            visited.remove((r,c))

        for r in range(0, rows):
            for c in range(0, cols):
                dfs(r, c, root, "")

        return list(res)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, best):
            if not node:
                return 0
            good = 1 if node.val >= best else 0
            best = max(best, node.val)
            return good + dfs(node.left, best) + dfs(node.right, best)
        return dfs(root, float('-inf'))
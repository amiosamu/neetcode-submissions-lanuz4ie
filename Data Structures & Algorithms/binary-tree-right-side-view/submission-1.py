# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        temp = []
        res = []
        queue = collections.deque([root])
        while queue:
            treeLevel = []
            for _ in range (len(queue)):
                node  = queue.popleft()
                treeLevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            temp.append(treeLevel)
        for t in temp:
            res.append(t[-1])
        return res



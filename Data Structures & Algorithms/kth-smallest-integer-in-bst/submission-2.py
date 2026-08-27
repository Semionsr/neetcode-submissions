# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        total = k
        result = root.val

        def dfs(node):
            if not node:
                return
            nonlocal total, result

            dfs(node.left)
            total -= 1
            if total == 0:
                result = node.val
                return
            dfs(node.right)
        dfs(root)
        return result

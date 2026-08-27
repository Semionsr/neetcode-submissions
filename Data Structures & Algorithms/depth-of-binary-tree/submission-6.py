# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(root):
            if not root:
                return 0
            
            nonlocal total

            maxleft = dfs(root.left)
            maxright = dfs(root.right)

            

            return 1 + max(maxleft,maxright)
        return dfs(root)

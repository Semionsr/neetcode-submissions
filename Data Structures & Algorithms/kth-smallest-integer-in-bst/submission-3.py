class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None

        def inorder(node):
            nonlocal k, res
            if not node or res is not None:
                return

            inorder(node.left)

            k -= 1
            if k == 0:
                res = node.val
                return

            inorder(node.right)

        inorder(root)
        return res

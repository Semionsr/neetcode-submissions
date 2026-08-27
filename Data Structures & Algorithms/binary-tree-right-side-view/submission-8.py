# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qlen = len(q)
            for i in range(qlen):
                rightmost = q.popleft()
                if rightmost:
                    if rightmost.left:
                        q.append(rightmost.left)
                    if rightmost.right:
                        q.append(rightmost.right)
            if rightmost:
                res.append(rightmost.val)
        return res




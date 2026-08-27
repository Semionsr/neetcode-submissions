# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qlen = len(q)
            cur = []
            for i in range(qlen):
                num = q.popleft()
                if num:
                    cur.append(num.val)
                    q.append(num.left)
                    q.append(num.right)
            if cur:
                res.append(cur)
        
        return res
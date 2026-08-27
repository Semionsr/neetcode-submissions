# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()

        q.append(root)
        res = []
        if not root:
            return []

        while q:
            lenq = len(q)
            total = []

            for i in range(lenq):
                checker = q.popleft()
                if checker:
                    if checker.left:
                        q.append(checker.left)
                    if checker.right:
                        q.append(checker.right)
                
                    total.append(checker.val)
                
            res.append(total)
        
        return res
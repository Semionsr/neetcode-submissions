# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        final = []
        rightmost = 0

        while q:
            qlen = len(q)

            for i in range(qlen):
                node = q.popleft()
                if node:
                    rightmost = node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if rightmost:
                final.append(rightmost)
        
        return final
        
                

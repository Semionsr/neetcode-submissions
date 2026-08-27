# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # base case
        if not root:
            return []
        #create a queue due to bfs and to pop left values
        q = collections.deque()
        q.append(root)
        res = []
        #iterating through the queue
        while q:
            qlen = len(q)
            rightmost = None
            #iterating through the levels of the tree
            for i in range(qlen):
                node = q.popleft()
                if node:
                    rightmost = node
                    q.append(node.left)
                    q.append(node.right)
            if rightmost:
                res.append(rightmost.val)
        return res

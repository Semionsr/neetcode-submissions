# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #stores the value not the key itself
        res = [root.val]

        # return max value without splitting

        def dfs(root):
            #base case
            if not root:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            #make sure that the value isnt negative
            leftMax = max(leftMax,0)
            rightMax = max(rightMax,0)
            
            #updates the max of a split
            res[0] = max(res[0], root.val + leftMax + rightMax)
            return (root.val + max(rightMax, leftMax))
        
        dfs(root)
        return res[0]
        
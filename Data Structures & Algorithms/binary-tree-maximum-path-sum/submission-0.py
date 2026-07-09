# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        # at each node you have the option of left, right, or None
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            #find the max path to the left subtree and right 
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            #getting rid of negative paths
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            #this is the best path through that node
            res = max(res, node.val + leftMax + rightMax)

            #this is the best extendable downward path
            return node.val + max(leftMax, rightMax)
        
        dfs(root)
        return res


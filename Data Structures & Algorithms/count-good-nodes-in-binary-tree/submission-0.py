# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        global goodnodes
        goodnodes = 0
        def dfs(node, maxVal):
            global goodnodes
            if not node:
                return 
            
            if node.val >= maxVal:
                goodnodes += 1
            
            dfs(node.right, max(maxVal, node.val))
            dfs(node.left, max(maxVal, node.val))
        
        dfs(root, root.val)

        return goodnodes

        
        
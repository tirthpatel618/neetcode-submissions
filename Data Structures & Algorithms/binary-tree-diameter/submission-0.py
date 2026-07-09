diameter = 0

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global diameter
        diameter = 0

        def height(node):
            global diameter
            if not node:
                return 0
            
            left = height(node.left)
            right = height(node.right)

            diameter = max(diameter, left + right)

            return 1 + max(left, right)
        
        height(root)
        return diameter
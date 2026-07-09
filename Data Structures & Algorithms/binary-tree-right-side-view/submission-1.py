# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # per level you can see at 1. 
        #The right most node should be the one at the end of queue


        queue = deque([root])
        res = []

        while queue:
            size = len(queue)
            #at the end of size nodes you should see the right most node
            for i in range(size):
                node = queue.popleft()
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                if i == size - 1 and node:
                    res.append(node.val)
        return res

                





        
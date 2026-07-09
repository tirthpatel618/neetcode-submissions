"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # keep a mapping of which nodes have already been cloned
        oldToNew = {}

        def clone(node):
            # if the clone we want to clone has already been cloned, return the clone
            if node in oldToNew:
                return oldToNew[node]

            # clone the node and add it to the dict
            newNode = Node(node.val)
            oldToNew[node] = newNode

            # clone all of its neighbors
            for neighbor in node.neighbors:
                newNode.neighbors.append(clone(neighbor))
            return newNode
        return clone(node) if node else None
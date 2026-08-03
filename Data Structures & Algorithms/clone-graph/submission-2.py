"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        The main thing to learn is that here we track the cloneed items with a dict 
        AND when making a deep copy you dont modify the original ever 
        """
        if not node:
            return None
        
        cloned = {}
        """
        dfs takes a node 

        the goal is to check if the node is already clone and if so return the clone 
        otherwise clone it and its neighbors 

        we reutnr the cloned object by just returning it 
        """
        def dfs(n):
            if n in cloned:
                return cloned[n]

            # clone the current one 
            cloned[n] = Node(n.val)

            # clone the neighbors (which is a list)
            for neighbor in n.neighbors:
                cloned[n].neighbors.append(dfs(neighbor))
            return cloned[n]
        return dfs(node)

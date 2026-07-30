"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        cloned = {}  # original node -> cloned node
        
        def dfs(n):
            if n in cloned:
                return cloned[n]  # already cloned, return existing clone
            
            # create the clone for this node
            clone = Node(n.val)
            cloned[n] = clone  # mark as visited by storing in map
            
            # clone all neighbors
            for neighbor in n.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)
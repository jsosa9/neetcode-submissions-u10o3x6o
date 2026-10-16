# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        not counting nodes but your counting the bridges you must corss thats 
        the length


        """
        self.total = 0
        def dfs(node):
            if node == None:
                return 0 
            else:
                l = dfs(node.left)
                r = dfs(node.right)
                self.total = max(self.total, l + r)
                return 1 + max(l,r)
        node = root
        dfs(node)
        return self.total

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        i know how to get the depth - the issue is i have to get the difference in depth of left and right
        """
        self.diff = 0 
        def dfs(node):
            if node == None:
                return 0
            else:
                l = dfs(node.left)
                r = dfs(node.right)
                if l == -1 or r == -1:
                    return -1 
                if abs(l - r) > 1:
                    return -1
                return 1 + max(l,r)
        
        x = dfs(root)
        if x == -1:
            return False
        else:
            return True



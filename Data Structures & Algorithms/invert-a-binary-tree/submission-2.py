# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        so similiar to reverse linked list 
        make the left the right and then make the right the left 
        """
        if not root:
            return None
        else:
            l = root.left
            r = root.right

            root.left = r 
            root.right = l

            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
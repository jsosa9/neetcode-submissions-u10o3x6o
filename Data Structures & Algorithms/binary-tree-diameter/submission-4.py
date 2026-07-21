# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        so diameter is max depth but with left depth + right depth 
        so we need to get the depth individually and then return it 
        """

        self.total = 0 
        def depth(node):
            if not node:
                return 0
            else: 
                l = depth(node.left)
                r = depth(node.right)

                self.total = max(self.total, l + r)
                return 1 + max(l, r)
        depth(root)
        return self.total

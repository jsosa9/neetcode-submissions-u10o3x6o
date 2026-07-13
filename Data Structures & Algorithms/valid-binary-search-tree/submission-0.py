# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, min_val, max_val):
            if not node:
                return True
            else:
                if node.val <= min_val or node.val >= max_val:
                    return False
                else:
                    return helper(node.left, min_val, node.val) and helper(node.right, node.val, max_val)
        return helper(root, float('-inf'), float('inf'))

        """
        for bst from the root the left side is counting down from root right side counts up
        so the left side the current node becomes the max since it gets smaller 
        the right side the current node becomes the min because its getting greater
        """
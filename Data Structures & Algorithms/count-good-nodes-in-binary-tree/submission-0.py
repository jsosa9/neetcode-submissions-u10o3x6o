# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, top):
            if not node:
                return 0
            is_good = 1 if node.val >= top else 0
            topp = max(top, node.val)
            return is_good + helper(node.left, topp) + helper(node.right, topp)


        return helper(root, root.val)
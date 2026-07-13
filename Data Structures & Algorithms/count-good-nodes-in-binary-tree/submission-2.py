# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, top):
            if not root:
                return 0
            else:
                is_good = 1 if root.val >= top else 0
                topp = max(top, root.val)
                return is_good + helper(root.left, topp) + helper(root.right, topp)
        return helper(root, root.val)
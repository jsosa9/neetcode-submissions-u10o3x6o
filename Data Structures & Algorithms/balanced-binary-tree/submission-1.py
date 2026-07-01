# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        so for every node the difference between the length of the right and left node
        cannot be more then 1 
        """
        self.total = 0
        def check(node):
            if node == None:
                return 0
            left = check(node.left)
            right = check(node.right)
            if left >= right:
                self.total = max(self.total, left - right)
            if right > left:
                self.total = max(self.total, right - left)
            return 1 + max(left, right)

        check(root)
        if self.total > 1:
            return False
        else:
            return True

            
        
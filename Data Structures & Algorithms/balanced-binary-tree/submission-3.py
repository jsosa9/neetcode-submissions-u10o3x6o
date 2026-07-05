# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        so for every node the difference in the height of the left and right cannot be more thne 1 

        so if there is a left and right for the node we need to incremement 
        and then determine whether the diff is more hten 1 
        if so we return false otherwise just reutnr true and continue 
        """
        def helper(root):
            if root:
                left = helper(root.left)
                right = helper(root.right)
                if left == -1 or right == -1:
                    return -1
                left += 1
                right += 1 
                diff = abs(left - right)
                h = max(left, right)
                if diff > 1:
                    return -1 
                else:
                    return h
            else:
                return 0
        x = helper(root)
        if x == -1:
            return False
        else:
            return True

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        so this is dfs 
        we're checking if the left and right side of the tree depth only differ by 1 at most 

        so we get the depth for each side and then get that as a number and 
        do math to check before conitnuing each time if the diff is more thne 1 
        """
        def helper(node):
            if not node:
                return 0
            else:
                x = helper(node.left)
                y = helper(node.right)
                if x == -1 or y == -1:
                    return -1
                z = abs(x - y)
                if z >= 2:
                    return -1
                else:
                    # return helper(node.left) and helper(node.right)
                    return 1 + max(x, y)
        # return helper(root)
        w = helper(root)
        if w == -1:
            return False
        else:
            return True

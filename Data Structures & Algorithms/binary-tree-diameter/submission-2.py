# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        so we need to for every node track its depth adn use max to update the 
        count once the left and right node hits null

        then we do the same for every node and then return the top count 

        so we need to picik a node starting at root 
        we run the max depth until both hit null 
        we update top 
        then we increment the node 
        repeat 
        in the end once the node we're starting from is null both are we return top
        """
        self.diameter = 0
        def depthHelp(root):
            if root:
                top = 1 + max(depthHelp(root.left), depthHelp(root.right))
                right = depthHelp(root.left)
                left = depthHelp(root.right)
                self.diameter = max(self.diameter, left + right)
                return 1 + max(left, right)
            else:
                return 0

        depthHelp(root)
        return self.diameter
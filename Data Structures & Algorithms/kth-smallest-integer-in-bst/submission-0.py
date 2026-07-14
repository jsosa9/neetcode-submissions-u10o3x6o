# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        thinking dfs because it goes top to bottom and helps maintain order
        we need kth smallest so we can have a array that does comparaisons and we do an array until 
        the size of it gets to k then we just return the top element 

        if the amount of nodes are less then k then we return -1 

        it says its 1 indexed tree so we have to account for that when making the array 
        """
        stack = []
        curr = root
        count = 0
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            count += 1
            if count == k:
                return curr.val
            curr = curr.right
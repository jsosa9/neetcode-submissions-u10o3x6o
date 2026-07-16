# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
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
            """
            so we add as much as possibel into the stack from the left 
            and then we pop and update count and check if the current count is k 
            if so reutnr the value 
            else continue 
            then wehn we continue we make curr the right which goes back to the while curr and it repeeats 
            and when there is no curr it will run the outside of the loop 
            """


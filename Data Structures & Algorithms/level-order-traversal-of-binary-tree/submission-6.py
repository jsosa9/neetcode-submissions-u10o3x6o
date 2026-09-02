# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        so we add the current one to the array its value and then we take its neighbors put those in the queue repeat
        """
        if root is None:
            return []
        re = []
        queue = deque()
        queue.append(root)
        while queue:
            t = []
            for _ in range(len(queue)):
                node = queue.popleft()
                t.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            re.append(t)
        return re
            
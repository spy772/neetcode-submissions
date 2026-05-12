# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = []
        if not root:
            return None
        
        queue.append(root)

        while queue:
            node = queue.pop(0)
            left = None
            right = None
            if node.left:
                queue.append(node.left)
                left = node.left
            if node.right:
                queue.append(node.right)
                right = node.right
            
            node.left = right
            node.right = left

        return root
            
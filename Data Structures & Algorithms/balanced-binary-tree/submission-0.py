# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        height_l = self.get_height(root.left)
        height_r = self.get_height(root.right)
        
        if abs(height_l - height_r) > 1:
            return False
        
        bal_l = self.isBalanced(root.left)
        bal_r = self.isBalanced(root.right)

        return bal_l and bal_r


    def get_height(self, subt_root: Optional[TreeNode]) -> int:
        if not subt_root:
            return 0
        
        return 1 + max(self.get_height(subt_root.left), self.get_height(subt_root.right))
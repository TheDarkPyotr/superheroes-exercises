
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
        return self.mirrorTree(root.left, root.right)
        
        
        
    def mirrorTree(self, left, right):
        
        if left and right:
            if left.val == right.val:
                left_sub = self.mirrorTree(left.left, right.right)
                right_sub = self.mirrorTree(left.right, right.left)
                return left_sub and right_sub
            return False
            
            
        else:
            if not left and not right:
                return True
            return False
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        return self.compareTree(p,q)
        
    def compareTree(self, node1, node2):
        
        if node1 and node2:
            
            if node1.val == node2.val:
                left_subtree = self.compareTree(node1.left, node2.left)
                right_subtree = self.compareTree(node1.right, node2.right)
                
                return left_subtree and right_subtree
            else:
                return False
        else:
            if not node1 and not node2:
                return True
            return False
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.maxSum = float('-inf')
        self.pathSum(root)
        return self.maxSum

    def pathSum(self, node):
            if node:
                left_sum = max(self.pathSum(node.left),0)
                right_sum = max(self.pathSum(node.right),0)

                current_sum = left_sum+right_sum+node.val
                self.maxSum = max(self.maxSum, current_sum)
                return node.val + max(left_sum, right_sum)

            return 0
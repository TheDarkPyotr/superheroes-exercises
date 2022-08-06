# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        #(level, node)
        queue = [(0, root)]
        result = 0

        while queue:
            level = []

            for _ in range(len(queue)):
                lvl, node = queue.pop(0)
                level.append(lvl)

                if node.left:
                    queue.append((2*lvl+1), node.left)
                if node.right:
                    queue.append((2*lvl+2, node.right))
            
            result = max(result, max(level) - min(level)+1)
        
        return result
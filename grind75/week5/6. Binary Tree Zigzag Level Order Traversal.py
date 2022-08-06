# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        level_way = 0
        queue = [root]
        result = []
        
        while queue:
            
            level = []
            
            for _ in range(len(queue)):
                
                node = queue.pop(0)
                if node:
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)
                
            level_way += 1
            if len(level) > 0: #evita inserimento lista vuota in result (edge case)
                if level_way % 2 == 0:
                    result.append(level[::-1])
                else:
                    result.append(level)
        
        return result
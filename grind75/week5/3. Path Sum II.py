# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.result = []
        self.recursiveSum(root,targetSum,[])
        return self.result
        
    def recursiveSum(self, node, target, path):
        
        if node:
          
            if target - node.val == 0:
                
                if node.left is None and node.right is None:
                    self.result.append(path + [node.val]) 
                    #print("Node {} path {}".format(node.val, path))
                    return
                 
            
            self.recursiveSum(node.left, target-node.val, path+[node.val])
            self.recursiveSum(node.right, target-node.val, path+[node.val])
            
            
        return []
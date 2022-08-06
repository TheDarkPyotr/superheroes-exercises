class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        self.pathCount = 0
        self.original = targetSum
        self.recursivePath(root,True, targetSum)
      
        return self.pathCount
        
    def recursivePath(self, node, startNode, target):
        
        if node:
            
            if target - node.val == 0:
                self.pathCount += 1
            
            #se ho rimosso nodo iniziale, continuo a rimuovere
            self.recursivePath(node.left,False, target-node.val)
            self.recursivePath(node.right,False, target-node.val)
            
            if startNode: #se path "nuovo", senza rimuovere node.val da target allora continuo
                
                self.recursivePath(node.left,True, self.original)
                self.recursivePath(node.right,True, self.original)
            
        return 
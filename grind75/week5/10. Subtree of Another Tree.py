class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            
            self.found = False
            self.searchSubtree(root, subRoot)
            return self.found
        
        
    def compareTree(self, node1, node2):
            
            if node1 and node2:
                
                if node1.val == node2.val:
                    left = self.compareTree(node1.left, node2.left)
                    right = self.compareTree(node1.right, node2.right)
                    return left and right
            else:
                if not node1 and not node2:
                    return True
                return False
        
        
    def searchSubtree(self, tree, subtree):
            
            if tree and subtree:
                if tree.val == subtree.val:
                    if self.compareTree(tree,subtree):
                        self.found = True
                        return
                    self.searchSubtree(tree.left, subtree)
                    self.searchSubtree(tree.right, subtree)
                
                else: 
                    self.searchSubtree(tree.left, subtree)
                    self.searchSubtree(tree.right, subtree)
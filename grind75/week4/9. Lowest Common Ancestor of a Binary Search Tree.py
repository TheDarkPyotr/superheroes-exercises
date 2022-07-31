class Solution:
    def lowestCommonAncestorIterative(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        while True:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root

    def lowestCommonAncestorRecursive(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

            cur_value = root.val
            
            if p.val > cur_value and q.val > cur_value:
                return self.lowestCommonAncestorRecursive( root.right, p, q)
            
            elif p.val < cur_value and q.val < cur_value:
                return self.lowestCommonAncestorRecursive( root.left, p, q)
            
            else:
                return root

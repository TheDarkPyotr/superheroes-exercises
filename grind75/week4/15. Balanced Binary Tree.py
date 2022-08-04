class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        
        def depth(node):
            if not node:
                return 0
            sx = depth(node.left)
            dx = depth(node.right)
            if abs(sx-dx) > 1 or sx == -1 or dx == -1:
                return -1
            height = max(sx,dx) + 1
            return height
        
        if depth(root) == -1:
            return False
        return True
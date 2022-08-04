#Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root, p):

        def inOrderTraversal(node):
            if node:
                left = inOrderTraversal(node.left)
                center = [node.val]
                right = inOrderTraversal(node.right)
                    
        ordered = inOrderTraversal(root)
        for i in range(len(ordered)):
            if ordered[i] > p.val:
                return ordered[i]


sol = Solution()
sol.inorderSuccessor()




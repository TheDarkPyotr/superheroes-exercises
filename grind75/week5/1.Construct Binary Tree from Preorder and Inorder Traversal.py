def buildTree(self, preorder, inorder):
    if inorder:
        root_index = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[root_index])
        root.left = self.buildTree(preorder, inorder[0:root_index])
        root.right = self.buildTree(preorder, inorder[root_index+1:])
        return root
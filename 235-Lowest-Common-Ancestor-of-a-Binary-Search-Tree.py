# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def lca(tree):
            if (tree.val == p.val or tree.val == q.val or
                tree.val > p.val and tree.val < q.val or
                tree.val < p.val and tree.val > q.val):
                return tree
            if tree.val < p.val and tree.val < q.val:
                return lca(tree.right)
            else:
                return lca(tree.left)
        
        return lca(root)


        
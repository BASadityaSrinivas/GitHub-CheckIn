# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        q = []
        q.append(root)

        while len(q) > 0:
            cur = q.pop(0)

            if cur:
                cur.left, cur.right = cur.right, cur.left

                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)

        return root
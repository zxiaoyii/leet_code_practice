# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def preOrder(node, p, q):
            if not node:
                return None
            if node == p or node == q:
                return node
            left = preOrder(node.left, p, q)
            right = preOrder(node.right, p, q)
            if left and right:
                return node
            elif left:
                return left
            elif right:
                return right
            else:
                return None
        return preOrder(root, p, q)
            
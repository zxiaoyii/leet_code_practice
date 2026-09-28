# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        mp = {value: i for i, value in enumerate(inorder)}
        self.i = 0

        def build(lo, hi):
            while lo > hi:
                return None
            root_v = preorder[self.i]
            self.i += 1
            root = TreeNode(root_v)
            mid = mp[root_v]
            root.left = build(lo, mid - 1)
            root.right = build(mid + 1, hi)
            return root
        return build(0, len(inorder) - 1)
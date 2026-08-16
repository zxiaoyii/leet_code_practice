# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, low , hi) -> bool:
            if not node:
                return True
            if low < node.val < hi:
                return dfs(node.left, low, node.val) and dfs(node.right, node.val, hi)
            return False
        
        return dfs(root, float('-inf'), float('inf'))
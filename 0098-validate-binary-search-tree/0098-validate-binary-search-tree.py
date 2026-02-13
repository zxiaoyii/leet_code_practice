# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, hi, lo) -> bool:
            if not node:
                return True
            val = node.val
            if not lo < val < hi:
                return False
            return dfs(node.left, val, lo) and dfs(node.right, hi, val)
        
        return dfs(root, float('inf'), float('-inf'))
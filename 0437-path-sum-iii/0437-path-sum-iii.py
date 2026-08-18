# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int) # sum -> count
        prefix[0] = 1

        def dfs(node, s):
            if not node:
                return 0

            new_s = node.val + s
            count = prefix[new_s - targetSum]
            prefix[new_s] += 1
            count += dfs(node.left, new_s) + dfs(node.right, new_s) 
            prefix[new_s] -= 1
            return count
        
        return dfs(root, 0)
            

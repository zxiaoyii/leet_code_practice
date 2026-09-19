# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(node, cur):
            if not node:
                return 0
            cur += node.val
            res = prefix[cur - targetSum]

            prefix[cur] += 1
            res += dfs(node.left, cur)
            res += dfs(node.right, cur)
            prefix[cur] -= 1
            return res
        return dfs(root, 0)

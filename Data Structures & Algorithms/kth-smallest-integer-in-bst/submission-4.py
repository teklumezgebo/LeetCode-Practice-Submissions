# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(root, values):
            
            if not root:
                return

            values.append(root.val)

            dfs(root.left, values)
            
            dfs(root.right, values)

            return values

        values = dfs(root, [])

        values.sort()

        return values[k - 1]
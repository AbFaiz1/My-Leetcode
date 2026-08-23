# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None and root2 is not None:
                return False
            if root2 is None and root1 is not None:
                return False
            if root1.val != root2.val:
                return False
            choice1 = dfs(root1.left, root2.left)
            choice2 = dfs(root1.right, root2.right)
            return choice1 and choice2
        return dfs(p, q)

        
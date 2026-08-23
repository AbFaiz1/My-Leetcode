class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root):
            nonlocal ans
            if root is None:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            ans = max(ans, l + r)
            return max(l+1, r+1)
        dfs(root)
        return ans
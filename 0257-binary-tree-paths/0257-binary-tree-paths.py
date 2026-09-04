class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(root, temp):
            if root is None:
                return
            temp.append(root.val)
            if root.left is None and root.right is None:
                ans.append("->".join(map(str, temp)))
                temp.pop()
                return
            dfs(root.left, temp)
            dfs(root.right, temp)
            temp.pop()
        dfs(root, []) 
        return ans
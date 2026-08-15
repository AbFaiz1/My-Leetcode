class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def dfs(root, s):
            if root is None:
                return

            s.append(str(root.val))

            if root.left is None and root.right is None:  
                ans.append("->".join(s))  
                s.pop()  
                return

            dfs(root.left, s)
            dfs(root.right, s)

            s.pop()  

        dfs(root, [])
        return ans
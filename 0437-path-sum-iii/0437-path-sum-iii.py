# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        mp = {0: 1}
        count  = 0
        def dfs(root, currSum):
            nonlocal mp
            nonlocal count
            if root is None:
                return 0
            currSum += root.val
            find = currSum - target
            if find in mp:
                count += mp[find]
            mp[currSum] = mp.get(currSum, 0)+1
            dfs(root.left, currSum)
            dfs(root.right, currSum)
            mp[currSum] -= 1
            currSum -= root.val
        dfs(root, 0)
        return count
            
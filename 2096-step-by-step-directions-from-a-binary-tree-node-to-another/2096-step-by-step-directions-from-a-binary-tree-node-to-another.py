class Solution:
    def getDirections(self, root: Optional[TreeNode], start: int, end: int) -> str:
        founds = []
        founde = []

        def finds(root, temp, start):
            if root is None:
                return False

            if root.val == start:
                founds.extend(temp)
                return True

            temp.append("L")
            if finds(root.left, temp, start):
                return True
            temp.pop()

            temp.append("R")
            if finds(root.right, temp, start):
                return True
            temp.pop()

            return False

        def finde(root, temp, end):
            if root is None:
                return False

            if root.val == end:
                founde.extend(temp)
                return True

            temp.append("L")
            if finde(root.left, temp, end):
                return True
            temp.pop()

            temp.append("R")
            if finde(root.right, temp, end):
                return True
            temp.pop()

            return False

        finds(root, [], start)
        finde(root, [], end)

        i = 0
        while i < len(founds) and i < len(founde) and founds[i] == founde[i]:
            i += 1

        ans = "U" * (len(founds) - i)
        ans += "".join(founde[i:])

        return ans
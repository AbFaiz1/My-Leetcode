class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, i):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return False

            if board[r][c] != word[i]:
                return False

            if i == len(word) - 1:
                return True

            temp = board[r][c]
            board[r][c] = "#"

            for x, y in directions:
                nr = r + x
                nc = c + y

                if dfs(nr, nc, i + 1):
                    board[r][c] = temp
                    return True

            board[r][c] = temp
            return False

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False
class TrieNode:
    def __init__(self):
        self.map = {}
        self.isEnd = False
        self.word = ""
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.map:
                curr.map[ch] = TrieNode()
            curr = curr.map[ch]
        curr.isEnd = True
        curr.word = word
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = []
        trie = Trie()
        for word in words:
            trie.insert(word)
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]
        rows = len(board)
        cols = len(board[0])
        visited = set()
        def dfs(r, c, node):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited:
                return 
            ch = board[r][c]
            if ch not in node.map:
                return 
            node = node.map[ch]
            if node.isEnd:
                ans.append(node.word)
                node.isEnd = False
            visited.add((r, c))
            for x, y in directions:
                nr = x + r
                nc = y + c
                dfs(nr, nc, node)
            visited.remove((r, c))
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, trie.root)
        return ans
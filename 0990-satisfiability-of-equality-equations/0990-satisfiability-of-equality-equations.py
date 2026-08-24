class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {
            'a': 'a',
            'b': 'b',
            'c': 'c',
            'd': 'd',
            'e': 'e',
            'f': 'f',
            'g': 'g',
            'h': 'h',
            'i': 'i',
            'j': 'j',
            'k': 'k',
            'l': 'l',
            'm': 'm',
            'n': 'n',
            'o': 'o',
            'p': 'p',
            'q': 'q',
            'r': 'r',
            's': 's',
            't': 't',
            'u': 'u',
            'v': 'v',
            'w': 'w',
            'x': 'x',
            'y': 'y',
            'z': 'z'
        }
        def find(x):
            if parent[x] == x:
                return x
            return find(parent[x])
        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                parent[py] = px
        for i in range(len(equations)):
            px = find(equations[i][0])
            py = find(equations[i][3])
            if equations[i][1:3] == "==" and px != py:
                union(equations[i][0], equations[i][3])
        for i in range(len(equations)):
            px = find(equations[i][0])
            py = find(equations[i][3])
            if equations[i][1:3] == "==":
                if px != py:
                    return False
            else:
                if px == py:
                    return False
        return True


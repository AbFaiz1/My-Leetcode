class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        graph = {}
        name = {}

        for i in range(len(accounts)):

            root = accounts[i][1]

            name[root] = accounts[i][0]

            if root not in graph:
                graph[root] = []

            if len(accounts[i]) >= 2:  # FIX: single-email account bhi valid hai

                for j in range(2, len(accounts[i])):

                    node = accounts[i][j]

                    if node not in graph:
                        graph[node] = []  # FIX: child bhi graph node hai

                    graph[root].append(node)
                    graph[node].append(root)  # FIX: connection dono direction mein

        ans = []

        visited = set()

        def dfs(start, temp):

            if start in visited:
                return  # FIX: already processed node ko skip

            visited.add(start)
            temp.add(start)

            for nei in graph[start]:
                dfs(nei, temp)

        for i in range(len(accounts)):

            root = accounts[i][1]

            if root in visited:
                continue

            store = set()

            dfs(root, store)

            ans.append([name[root]] + sorted(store))

        return ans
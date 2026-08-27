class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        visit = set()

        for v,c in edges:
            adj[v].append(c)
            adj[c].append(v)
        



        def dfs(node, par):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True
                    

        return dfs(0, -1) and len(visit) == n
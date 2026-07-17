class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        edge_list = [[] for _ in range(n)]

        for u, v in edges:
            edge_list[u].append(v)
            edge_list[v].append(u)
        
        visited = set()
        q = deque()
        q.append((0, None))
        # visited.add(0)
        
        while q:
            cur, parent = q.popleft()
            if cur in visited:
                return False
            visited.add(cur)

            for neighbor in edge_list[cur]:
                if neighbor == parent:
                    continue
                q.append((neighbor, cur))
        
        return len(visited)==n
                

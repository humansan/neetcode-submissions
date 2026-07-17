class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        stack = []
        seen = set()

        adj_list = [[] for _ in range(n)]
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        count = 0

        for i in range(n):
            if i not in seen:
                count += 1

                stack.append(i)
                seen.add(i)

                while stack:
                    cur = stack.pop()

                    for neigh in adj_list[cur]:
                        if neigh not in seen:
                            seen.add(neigh)
                            stack.append(neigh)
        
        return count



            
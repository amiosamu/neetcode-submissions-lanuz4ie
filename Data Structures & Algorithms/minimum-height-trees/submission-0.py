class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = [0] * n
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1

        queue = deque()
        remaining = n
        for i in range(n):
            if degree[i] == 1:
                queue.append(i)
        
        while remaining > 2:
            size = len(queue)
            remaining -= size
            for _ in range(size):
                leaf = queue.popleft()
                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)
        return list(queue)


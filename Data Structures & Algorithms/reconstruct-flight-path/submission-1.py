class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        result = []
        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            result.append(airport)
        dfs('JFK')
        print(result[::-1])
        return result[::-1]
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-count for count in counts.values()]
        heapq.heapify(max_heap)

        task_queue = deque()
        t = 0

        while max_heap or task_queue:
            if not max_heap:
                t = task_queue[0][0]
            while task_queue and task_queue[0][0] <= t:
                _, count = task_queue.popleft()
                heapq.heappush(max_heap, count)
            
            task_count = -heapq.heappop(max_heap)
            task_count -= 1
            t += 1

            if task_count > 0:
                task_queue.append((t + n, -task_count))
        return t
            
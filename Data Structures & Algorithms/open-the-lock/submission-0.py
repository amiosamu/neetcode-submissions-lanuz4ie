class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if '0000' in dead:
            return -1
        queue = deque([('0000', 0)])
        visited = {'0000'}
        def get_neighbors(state):
            neighbors = []
            for i in range(4):
                digit = int(state[i])
                for d in [-1, 1]:
                    new_digit = (digit + d) % 10
                    new_state = state[:i] + str(new_digit) + state[i+1:]
                    neighbors.append(new_state)
            return neighbors

        while queue:
            state, steps = queue.popleft()

            if state == target:
                return steps

            for neighbor in get_neighbors(state):
                if neighbor not in visited and neighbor not in deadends:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
        return -1
        
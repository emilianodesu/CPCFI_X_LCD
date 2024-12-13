from collections import deque

def min_clicks(n, m):
    if n >= m:
        return n - m

    queue = deque([(m, 0)])  # (current number, number of clicks)
    visited = set([m])

    while queue:
        current, clicks = queue.popleft()

        if current == n:
            return clicks

        if current % 2 == 0 and current // 2 not in visited:
            queue.append((current // 2, clicks + 1))
            visited.add(current // 2)

        if current - 1 > 0 and current - 1 not in visited:
            queue.append((current - 1, clicks + 1))
            visited.add(current - 1)

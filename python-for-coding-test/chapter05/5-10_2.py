from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False

    if graph[x][y] == 0:
        queue = deque()
        queue.append((x, y))
        graph[x][y] = 1  # 방문 처리

        while queue:
            cx, cy = queue.popleft()
            # 상하좌우 탐색
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                    queue.append((nx, ny))
                    graph[nx][ny] = 1  # 방문 처리

        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if bfs(i, j):
            result += 1

print(result)
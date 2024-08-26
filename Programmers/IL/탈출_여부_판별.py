from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and graph[x][y] == 1

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        if x == n-1 and y == m-1:
            return True

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))

    return False

print(1 if bfs(0, 0) else 0)
from collections import deque

n, m = map(int, input().split())
graph = [list(map(str, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
cnt = 0

def can_go(x, y):
    return 0 <= x < n and 0 <= y < m and not visited[x][y] and graph[x][y] != 'X'

def bfs(x, y):
    global cnt
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        if graph[x][y] == 'P':
            cnt += 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True


for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I' and not visited[i][j]:
            bfs(i, j)
            break

print(cnt) if cnt > 0 else print('TT')
from collections import deque

while True:
    m, n = map(int, input().split())

    if m == 0 and n == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    dx, dy = [0, 1, 0, -1, 1, -1, 1, -1], [1, 0, -1, 0, -1, 1, 1, -1]
    lst = []


    def can_go(x, y):
        return 0 <= x < n and 0 <= y < m


    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[x][y] = True
        cnt = 1

        while q:
            x, y = q.popleft()

            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]

                if can_go(nx, ny) and not visited[nx][ny] and graph[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
        return cnt


    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 1:
                lst.append(bfs(i, j))
    print(len(lst))
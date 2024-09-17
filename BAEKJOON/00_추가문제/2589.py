from collections import deque

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
step = [[0]*m for _ in range(n)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
q = deque()

def can_go(x, y):
    return 0 <= x < n and 0 <= y < m

def push(x, y, s):
    step[x][y] = s
    visited[x][y] = True
    q.append((x, y))

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if can_go(nx, ny) and not visited[nx][ny] and graph[nx][ny] == 'L':
                push(nx, ny, step[x][y] + 1)

def find_max():
    tmp = 0
    for i in range(n):
        for j in range(m):
            tmp = max(tmp, step[i][j])
    return tmp

lst = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            # BFS 수행 전에 visited와 step 배열을 초기화
            visited = [[False]*m for _ in range(n)]
            step = [[0]*m for _ in range(n)]
            push(i, j, 0)
            bfs()
            lst.append(find_max())

print(max(lst))
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and graph[x][y] == 1

def dfs(x, y):
    visited[x][y] = 1
    dx = [1, 0]
    dy = [0, 1]

    for direction in range(2):
        nx, ny = x + dx[direction], y + dy[direction]

        if can_go(nx, ny):
            dfs(nx, ny)

# 초기값 설정
visited[0][0] = 1
dfs(0, 0)

print(visited[n-1][m-1])
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, visited):
    return in_range(x, y) and not visited[x][y] and graph[x][y] != -1

def dfs(x, y, visited):
    cnt = 1
    visited[x][y] = 1
    
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if can_go(nx, ny, visited):
            cnt += dfs(nx, ny, visited)

    return cnt

k = max(max(row) for row in graph)

result = []
for t in range(1, k + 1):
    # 각 단계별로 graph 갱신
    for i in range(n):
        for j in range(m):
            if graph[i][j] <= t:
                graph[i][j] = -1
    
    visited = [[0] * m for _ in range(n)]
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if can_go(i, j, visited):
                dfs(i, j, visited)
                cnt += 1
    
    result.append(cnt)

print(result.index(max(result))+1, max(result))
import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for x in graph:
    x.sort(reverse=True)

visited = [False] * (n+1)
result = [0] * (n+1)  # 방문 순서를 기록할 리스트
order = 1  # 방문 순서를 매길 변수

def dfs(v):
    global order
    visited[v] = True
    result[v] = order
    order += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(v)

for i in range(1, n+1):
    print(result[i])
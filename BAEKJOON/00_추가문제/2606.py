n = int(input())
m = int(input())

graph = [[False]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    x,y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

cnt = 0    
def dfs(v):
    global cnt
    visited[v] = True
    
    for i in range(1,n+1):
        if not visited[i] and graph[i][v] == 1:
            cnt += 1
            dfs(i)
dfs(1)                                 
print(cnt)
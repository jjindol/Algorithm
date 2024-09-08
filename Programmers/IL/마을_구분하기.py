n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and graph[x][y] == 1

def dfs(x,y):
    
    cnt = 1
    visited[x][y] = 1

    dx,dy = [1,0,-1,0],[0,1,0,-1]
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]

        if can_go(nx,ny):
            cnt += dfs(nx,ny)
    return cnt
            
result = []
for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and not visited[i][j]:
            result.append(dfs(i,j))
            
result.sort()

print(len(result))
for x in result:
    print(x)
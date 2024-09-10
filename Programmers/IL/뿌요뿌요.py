n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    return in_range(x,y) and not visited[x][y]

def dfs(x,y):

    block = 1
    visited[x][y] = 1

    dx,dy = [1,0,-1,0],[0,1,0,-1]
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]

        if can_go(nx,ny) and graph[x][y] == graph[nx][ny]:
            block += dfs(nx,ny)

    return block

result = []
bomb = 0
for i in range(n):
    for j in range(n):
        tmp = dfs(i,j)
        result.append(tmp)
        if tmp >= 4:
            bomb += 1

print(bomb, max(result))